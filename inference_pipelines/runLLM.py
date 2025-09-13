from vllm import LLM, SamplingParams
from argparse import ArgumentParser
import torch
from datasets import load_dataset
from DataUtils.Datasets import MinimalImageCADDataset
import os
from PIL import Image
import base64
from io import BytesIO
import json
from transformers import AutoTokenizer
import re
from Processors.SyntaxValidProcessor import SyntaxValidProcessor
import time
import random

args = ArgumentParser(description="Run a test with a VLLM compatible model")
args.add_argument("--model_path", type=str, required=True, help="Path to the model to be tested. Path can be a local directory or a Hugging Face model identifier.")
args.add_argument("--test_splits", type=str, default="test100,R400", help="Comma-separated list of dataset splits to test. Default: 'test100,R400'. Choice from 'test', 'R400', 'test100'.")
args.add_argument("--max_tokens", type=int, default=4096, help="Maximum length of the generated text. Default: 4096")
args.add_argument("--temperature", type=float, default=1.0, help="Sampling temperature. Default: 1.0")
args.add_argument("--top_p", type=float, default=0.8, help="Top-p sampling parameter. Default: 0.8")
args.add_argument("--n_samples", type=int, default=1, help="Number of samples to generate. Default: 1")
args.add_argument("--beam_width", type=int, default=None, help="Beam width for beam search. Default: None (no beam search, must be larger or equal to n_samples).")
args.add_argument("--tensor_parallel_size", type=int, default=None, help="Number of GPUs to use for tensor parallelism. Default: None (will use all available GPUs). If set, must be larger than 1.")
args.add_argument("--pipeline_parallel_size", type=int, default=1, help="Number of processes to use for pipeline parallelism. Default: 1")
args.add_argument("--dtype", type=str, default='bfloat16', help="Data type for the model. Default: 'bfloat16'. Options: 'float16', 'bfloat16', 'float32'")
args.add_argument("--save_path", type=str, default="results_.json", help="Path to save the results. Default: 'results.json'")
args.add_argument("--save_responses", action='store_true', help="Whether to save the responses as well. Default: False")
args.add_argument("--system_prompt", type=str, default="You are a helpful assistant", help="System prompt for the model. Default: 'You are a helpful assistant'")
args.add_argument("--n_workers", type=int, default=64, help="Number of parallel jobs to run for IOU calculation. Default: 64")
args.add_argument("--timeout", type=int, default=15, help="Timeout for IOU calculation in seconds. Default: 15s")
args.add_argument("--seed_json_script", type=str, default="seed_images", help="Timeout for IOU calculation in seconds. Default: 15s")
args.add_argument("--image_type", type=str, default="png", help="Timeout for IOU calculation in seconds. Default: 15s")

args = args.parse_args()

# Extracts code from model generated text
def extract_code(text):
    # Use regex to find the code block
    match = re.search(r'```python(.*?)```', text, re.DOTALL)
    if match:
        return match.group(1).strip()
    else:
        return ""

# Function that reads in a .py path and converts it to a string
def code_to_string(file_path: str) -> str:
    """
    Reads a Python file and returns its content as a string.
    """
    with open(file_path, 'r') as file:
        code = file.read()
    return code

def prepare_context(json_path: str = "docs_examples/examples.json", python_examples_dir: str = "docs_examples") -> str:
    """
    Prepare CadQuery context for the model using the CadQuery documentation.
    """
    
    with open(json_path, 'r') as f:
        dataset = json.load(f)
    
    full_context = ""
    for i, item in enumerate(dataset):
        code_as_str = code_to_string(os.path.join('docs_examples', item['code_path']))
        full_context += f"CadQuery Example: {item['title']}\n"
        full_context += f"{item['description']}\n"
        full_context += f"Code:\n```python\n{code_as_str}\n```\n"
    return full_context

def encode_image(image: Image.Image, im_type='jpeg') -> str:
        buffered = BytesIO()
        image.save(buffered, format=im_type)
        return base64.b64encode(buffered.getvalue()).decode("utf-8")

def main():
    
    start_time = time.time()
    
    # Load the json description
    with open(args.seed_json_script, 'r', encoding='utf-8') as f:
        data = json.load(f)

    list_of_descriptions =  [item.get('full_response') for item in data if isinstance(item, dict)]
    list_of_images = [item.get('image_path') for item in data if isinstance(item, dict)]
    
    # Prepare the prompts for the LLM based on json descriptions
    prompts = []

    for description in list_of_descriptions:
        user_prompt = f"You will generate CadQuery code to CAD an object. As a reminder, here are examples on how to use CadQuery syntax correctly.\n{prepare_context()}\nGenerate the CadQuery code for an object meeting the following description:\n {description} \nEnd your code by assigning the object to a variable named `result`."
        prompt = [
            {
                "role": "system",
                "content": [{"type": "text", "text": args.system_prompt}]
            },
            {
                "role": "user",
                "content": [{"type": "text", "text": user_prompt}]
            }
        ]
        prompts.append(prompt)
    
    print("SETTING UP LLM MODEL...")
    model = LLM(model=args.model_path,
                tensor_parallel_size=args.tensor_parallel_size if args.tensor_parallel_size else torch.cuda.device_count(),
                pipeline_parallel_size=args.pipeline_parallel_size,
                dtype=args.dtype)

    sampling_params = SamplingParams(
        temperature=args.temperature,
        top_p=args.top_p,
        max_tokens=args.max_tokens,
        n = args.n_samples,
        best_of = args.beam_width
    )

    print("RUNNING INFERENCE...")
    results = model.chat(prompts, sampling_params=sampling_params)
    end_time = time.time()
    
    # Process model responses to determine syntax validity
    final_set = []
    codes = []
    iou_set = []
    
    # Extract code
    for i, result in enumerate(results):
        for j in range(args.n_samples):
            just_code = extract_code(result.outputs[j].text).strip()
            codes.append(just_code)
            iou_set.append({
                'ground_truth': "",
                'generated': just_code
            })
            # print("Code generated:\n", just_code)

    iou_processor = SyntaxValidProcessor(num_workers=64, timeout=15)
    iou_scores, status_codes = iou_processor(iou_set)
    
    # Write results to file
    for i, result in enumerate(results):
        for j in range(args.n_samples):
            final_set.append({
                'full_response': result.outputs[j].text,
                'valid_syntax': int(iou_scores[i]),
                'code': codes[i],
                'image_path': list_of_images[i],
                'description': list_of_descriptions[i]
            })

    # Save data to a file
    with open(args.save_path, 'w') as f:
        json.dump(final_set, f, indent=4)  # indent=4 makes it more human-readable
        
    num_valid = iou_scores[iou_scores != -1].sum()
    total_num = len(iou_scores)
    print(f"{num_valid} out of {total_num} samples have valid syntax.")
    print(f"Full results saved to {args.save_path}")
    print(f"Total generation time taken: {end_time - start_time} seconds")
        
if __name__ == '__main__':
    main()
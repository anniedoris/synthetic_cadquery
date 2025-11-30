#!/usr/bin/env python3
"""
LLM Pipeline for Refining Structured CAD JSON to Valid CadQuery Code

This script takes structured JSON CAD representations from the VLM and uses an LLM
to generate valid, constraint-satisfying CadQuery code. The LLM can fix issues,
add missing operations, and ensure the code actually works.

Usage:
    python inference_pipelines/runLLM_from_structured_refined.py \
        --model_path Qwen/Qwen3-Coder-30B-A3B-Instruct \
        --seed_json_script object_structured.json \
        --save_path sdg_structured_refined.json
"""

from vllm import LLM, SamplingParams
from argparse import ArgumentParser
import torch
import json
import re
import time
from Processors.SyntaxValidProcessor import SyntaxValidProcessor

args = ArgumentParser(description="Refine structured CAD JSON to valid CadQuery code using LLM")
args.add_argument("--model_path", type=str, required=True, help="Path to the LLM model")
args.add_argument("--seed_json_script", type=str, required=True, help="Input JSON with structured CAD")
args.add_argument("--max_tokens", type=int, default=4096, help="Max tokens. Default: 4096")
args.add_argument("--temperature", type=float, default=1.0, help="Temperature. Default: 1.0")
args.add_argument("--top_p", type=float, default=0.8, help="Top-p. Default: 0.8")
args.add_argument("--n_samples", type=int, default=1, help="Number of samples. Default: 1")
args.add_argument("--beam_width", type=int, default=None, help="Beam width. Default: None")
args.add_argument("--tensor_parallel_size", type=int, default=None, help="Tensor parallel size")
args.add_argument("--pipeline_parallel_size", type=int, default=1, help="Pipeline parallel size")
args.add_argument("--dtype", type=str, default='bfloat16', help="Data type. Default: bfloat16")
args.add_argument("--save_path", type=str, default="sdg_structured_refined.json", help="Output path")
args.add_argument("--system_prompt", type=str, default="You are a helpful assistant", help="System prompt")
args.add_argument("--n_workers", type=int, default=64, help="Workers for validation. Default: 64")
args.add_argument("--timeout", type=int, default=15, help="Validation timeout. Default: 15s")

args = args.parse_args()

# Extract code from model generated text
def extract_code(text):
    match = re.search(r'```python(.*?)```', text, re.DOTALL)
    if match:
        return match.group(1).strip()
    else:
        return ""

# Function that reads in a .py path and converts it to a string
def code_to_string(file_path: str) -> str:
    with open(file_path, 'r') as file:
        code = file.read()
    return code

def prepare_context(json_path: str = "docs_examples/examples.json", python_examples_dir: str = "docs_examples") -> str:
    """Prepare CadQuery context using examples."""
    import os
    with open(json_path, 'r') as f:
        dataset = json.load(f)

    full_context = ""
    for i, item in enumerate(dataset):
        code_as_str = code_to_string(os.path.join('docs_examples', item['code_path']))
        full_context += f"CadQuery Example: {item['title']}\n"
        full_context += f"{item['description']}\n"
        full_context += f"Code:\n```python\n{code_as_str}\n```\n"
    return full_context

def create_prompt_from_structured_json(structured_cad: dict, image_path: str) -> str:
    """
    Create an LLM prompt that includes the structured JSON and asks the LLM
    to generate valid CadQuery code that satisfies all constraints.
    """

    json_str = json.dumps(structured_cad, indent=2) if structured_cad else "No structured data available"

    prompt = f"""You will generate CadQuery code based on a structured JSON representation from a vision model.

The vision model attempted to describe the CAD object with the following structured operations:

{json_str}

Your task:
1. Interpret this structured JSON representation
2. Generate valid CadQuery code that creates the described object
3. Fix any issues or missing information in the JSON
4. Ensure all operations are valid and constraints are satisfied
5. Add any necessary operations that may be missing
6. Make sure dimensions are reasonable and the code will execute

As a reminder, here are examples of correct CadQuery syntax:
{prepare_context()}

Generate the CadQuery code for the object described in the JSON above.
End your code by assigning the object to a variable named `result`.

Important:
- The JSON may be incomplete or have errors - use your judgment to create valid code
- Ensure all operations follow CadQuery syntax rules
- Make sure geometric constraints are satisfied (e.g., holes within bounds)
- The code must be executable and create valid 3D geometry"""

    return prompt

def main():
    start_time = time.time()

    # Load structured CAD JSON
    print("LOADING STRUCTURED CAD JSON...")
    with open(args.seed_json_script, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Filter for successfully parsed entries
    valid_entries = [item for item in data if item.get('parse_success', False)]
    print(f"Loaded {len(data)} entries, {len(valid_entries)} with valid structured JSON.")

    # If no valid entries, exit
    if not valid_entries:
        print("No valid structured JSON entries found. Exiting.")
        return

    # Prepare prompts for the LLM
    prompts = []
    list_of_structured_cad = []
    list_of_images = []

    for item in valid_entries:
        structured_cad = item.get('structured_cad')
        image_path = item.get('image_path', '')

        user_prompt = create_prompt_from_structured_json(structured_cad, image_path)
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
        list_of_structured_cad.append(structured_cad)
        list_of_images.append(image_path)

    print("SETTING UP LLM MODEL...")
    model = LLM(
        model=args.model_path,
        tensor_parallel_size=args.tensor_parallel_size if args.tensor_parallel_size else torch.cuda.device_count(),
        pipeline_parallel_size=args.pipeline_parallel_size,
        dtype=args.dtype
    )

    sampling_params = SamplingParams(
        temperature=args.temperature,
        top_p=args.top_p,
        max_tokens=args.max_tokens,
        n=args.n_samples,
        best_of=args.beam_width
    )

    print("RUNNING LLM INFERENCE...")
    results = model.chat(prompts, sampling_params=sampling_params)
    end_time = time.time()

    # Process model responses
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

    print("VALIDATING GENERATED CODE...")
    iou_processor = SyntaxValidProcessor(num_workers=args.n_workers, timeout=args.timeout)
    iou_scores, status_codes = iou_processor(iou_set)

    # Write results to file
    for i, result in enumerate(results):
        for j in range(args.n_samples):
            final_set.append({
                'full_response': result.outputs[j].text,
                'valid_syntax': int(iou_scores[i]),
                'code': codes[i],
                'image_path': list_of_images[i],
                'structured_cad': list_of_structured_cad[i],
                'description': list_of_structured_cad[i].get('description', '') if list_of_structured_cad[i] else ''
            })

    # Save data to a file
    with open(args.save_path, 'w') as f:
        json.dump(final_set, f, indent=2)

    num_valid = iou_scores[iou_scores != -1].sum()
    total_num = len(iou_scores)

    print(f"\n{'='*60}")
    print(f"Results saved to {args.save_path}")
    print(f"{num_valid} out of {total_num} samples have valid syntax.")
    print(f"Total generation time: {end_time - start_time:.2f} seconds")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()

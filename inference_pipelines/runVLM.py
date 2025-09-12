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
import time
import random

args = ArgumentParser(description="Run a test with a VLLM compatible model")
args.add_argument("--model_path", type=str, required=True, help="Path to the model to be tested. Path can be a local directory or a Hugging Face model identifier.")
args.add_argument("--max_tokens", type=int, default=4096, help="Maximum length of the generated text. Default: 4096")
args.add_argument("--temperature", type=float, default=1.0, help="Sampling temperature. Default: 1.0")
args.add_argument("--top_p", type=float, default=0.8, help="Top-p sampling parameter. Default: 0.8")
args.add_argument("--n_samples", type=int, default=1, help="Number of samples to generate. Default: 1")
args.add_argument("--beam_width", type=int, default=None, help="Beam width for beam search. Default: None (no beam search, must be larger or equal to n_samples).")
args.add_argument("--tensor_parallel_size", type=int, default=None, help="Number of GPUs to use for tensor parallelism. Default: None (will use all available GPUs). If set, must be larger than 1.")
args.add_argument("--pipeline_parallel_size", type=int, default=1, help="Number of processes to use for pipeline parallelism. Default: 1")
args.add_argument("--dtype", type=str, default='bfloat16', help="Data type for the model. Default: 'bfloat16'. Options: 'float16', 'bfloat16', 'float32'")
args.add_argument("--save_path", type=str, default="results_.json", help="Path to save the results. Default: 'results.json'")
args.add_argument("--system_prompt", type=str, default="You are a helpful assistant", help="System prompt for the model. Default: 'You are a helpful assistant'")
args.add_argument("--user_prompt", type=str, default="Describe the CAD object(s) in the image to the best of your ability. First, provide a high level description of what you think the object is. Then, provide a detailed description of the geometric features present in the object, such that I could sketch or CAD the object if desired. Do not have your description reference specific CAD softwares/buttons.", help="User prompt for the model. Default: 'Generate the CADQuery code needed to create the CAD for the provided image.'")
args.add_argument("--seed_images", type=str, default="seed_images", help="Timeout for IOU calculation in seconds. Default: 15s")
args.add_argument("--image_type", type=str, default="png", help="Timeout for IOU calculation in seconds. Default: 15s")

args = args.parse_args()

def encode_image(image: Image.Image, im_type='jpeg') -> str:
        buffered = BytesIO()
        image.save(buffered, format=im_type)
        return base64.b64encode(buffered.getvalue()).decode("utf-8")

def main():
    
    # Time VLM generation time
    start_time = time.time()
    
    # Load images for the VLM
    print("LOADING IMAGES...")
    image_files = os.listdir(args.seed_images)
    print(f"Found {len(image_files)} images.")

    # Prepare images for inference
    images = []
    for fname in image_files:
        path = os.path.join(args.seed_images, fname)
        img = Image.open(path)
        images.append(img)
    
    # Prepare prompts for the VLM
    print("LOADING PROMPTS:")
    prompts = []

    for image in images:
        prompt = [
            {
                "role": "system",
                "content": [{"type": "text", "text": args.system_prompt}]
            },
            {
                "role": "user",
                "content": [{"type": "image_url", "image_url": {"url": f"data:image/{args.image_type};base64,{encode_image(image, im_type=args.image_type)}"}},
                            {"type": "text", "text": args.user_prompt}]
            }
        ]
        prompts.append(prompt)
        
    print("SETTING UP VLLM MODEL...")
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
    
    final_set = []
    for i, result in enumerate(results):
        for j in range(args.n_samples):
            entry = {
                'full_response': result.outputs[j].text,
                'image_path': image_files[i]
            }
            final_set.append(entry)

    with open(args.save_path, 'w') as f:
        json.dump(final_set, f, indent=4)  # indent=4 makes it more human-readable
        
    print(f"Results saved to {args.save_path}")
    end_time = time.time()
    print(f"Total time taken for SDG: {end_time - start_time:.2f} seconds")
        
if __name__ == '__main__':
    main()
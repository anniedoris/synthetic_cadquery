#!/usr/bin/env python3
"""
VLM Pipeline for Structured CAD Output

This script prompts a VLM to output structured JSON representations of CAD objects
instead of natural language descriptions.

Usage:
    python inference_pipelines/runVLM_structured.py \
        --model_path Qwen/Qwen2.5-VL-72B-Instruct \
        --seed_images data/sdg_abc_1k_images \
        --save_path object_structured.json
"""

from vllm import LLM, SamplingParams
from argparse import ArgumentParser
import torch
from PIL import Image
import base64
from io import BytesIO
import json
import time

args = ArgumentParser(description="Run VLM with structured CAD output")
args.add_argument("--model_path", type=str, required=True, help="Path to the model")
args.add_argument("--max_tokens", type=int, default=4096, help="Maximum tokens. Default: 4096")
args.add_argument("--temperature", type=float, default=0.7, help="Sampling temperature. Default: 0.7")
args.add_argument("--top_p", type=float, default=0.9, help="Top-p sampling. Default: 0.9")
args.add_argument("--n_samples", type=int, default=1, help="Number of samples. Default: 1")
args.add_argument("--beam_width", type=int, default=None, help="Beam width. Default: None")
args.add_argument("--tensor_parallel_size", type=int, default=None, help="Tensor parallel size")
args.add_argument("--pipeline_parallel_size", type=int, default=1, help="Pipeline parallel size")
args.add_argument("--dtype", type=str, default='bfloat16', help="Data type: bfloat16/float16/float32")
args.add_argument("--save_path", type=str, default="object_structured.json", help="Output JSON path")
args.add_argument("--seed_images", type=str, required=True, help="Path to seed images directory")
args.add_argument("--image_type", type=str, default="png", help="Image type. Default: png")
args.add_argument("--system_prompt", type=str, default="You are a CAD expert that analyzes 3D objects and outputs structured JSON representations.", help="System prompt")

args = args.parse_args()

# Schema definition embedded in the prompt
SCHEMA_EXAMPLE = """{
  "workplane": "XY",
  "description": "A simple rectangular plate with rounded edges",
  "operations": [
    {
      "type": "sketch",
      "shapes": [
        {
          "shape": "rect",
          "width": 10.0,
          "height": 5.0,
          "centered": true
        }
      ]
    },
    {
      "type": "extrude",
      "distance": 2.0
    },
    {
      "type": "fillet",
      "radius": 0.5,
      "selector": "|Z"
    }
  ]
}"""

USER_PROMPT_TEMPLATE = """Analyze this CAD object image and provide a structured JSON representation that describes how to construct it using CAD operations.

Your response must be a valid JSON object following this structure:
- "workplane": The initial workplane ("XY", "YZ", "XZ", etc.)
- "description": Brief description of what the object is
- "operations": Array of operations in sequence

Available operations:
1. sketch: Define 2D shapes (rect, circle, polygon, polyline)
   - rect: {{"shape": "rect", "width": X, "height": Y}}
   - circle: {{"shape": "circle", "radius": R}}
   - polygon: {{"shape": "polygon", "nSides": N, "diameter": D}}
   - polyline: {{"shape": "polyline", "points": [[x1,y1], [x2,y2], ...], "closed": true/false}}

2. extrude: {{"type": "extrude", "distance": D}}
3. cut: {{"type": "cut", "distance": D}}
4. hole: {{"type": "hole", "diameter": D, "depth": H, "positions": [[x1,y1], [x2,y2]]}}
5. fillet: {{"type": "fillet", "radius": R, "selector": "|Z"}}
6. chamfer: {{"type": "chamfer", "length": L}}
7. rotate: {{"type": "rotate", "axisStart": [x,y,z], "axisEnd": [x,y,z], "angle": degrees}}
8. translate: {{"type": "translate", "offset": [x,y,z]}}
9. mirror: {{"type": "mirror", "mirrorPlane": "XY"/"YZ"/"XZ", "union": true/false}}
10. shell: {{"type": "shell", "thickness": T}}
11. workplane_on_face: {{"type": "workplane_on_face", "face_selector": ">Z"}}

Example output:
{schema_example}

Analyze the image and output ONLY the JSON (no additional text):"""

def encode_image(image: Image.Image, im_type='png') -> str:
    buffered = BytesIO()
    image.save(buffered, format=im_type)
    return base64.b64encode(buffered.getvalue()).decode("utf-8")

def main():
    start_time = time.time()

    # Load images
    print("LOADING IMAGES...")
    import os
    image_files = sorted([f for f in os.listdir(args.seed_images)
                         if f.lower().endswith(('.png', '.jpg', '.jpeg'))])
    print(f"Found {len(image_files)} images.")

    images = []
    for fname in image_files:
        path = os.path.join(args.seed_images, fname)
        img = Image.open(path)
        images.append(img)

    # Prepare prompts
    print("PREPARING PROMPTS...")
    prompts = []
    user_prompt = USER_PROMPT_TEMPLATE.format(schema_example=SCHEMA_EXAMPLE)

    for image in images:
        prompt = [
            {
                "role": "system",
                "content": [{"type": "text", "text": args.system_prompt}]
            },
            {
                "role": "user",
                "content": [
                    {"type": "image_url", "image_url": {"url": f"data:image/{args.image_type};base64,{encode_image(image, im_type=args.image_type)}"}},
                    {"type": "text", "text": user_prompt}
                ]
            }
        ]
        prompts.append(prompt)

    print("SETTING UP VLM MODEL...")
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

    print("RUNNING INFERENCE...")
    results = model.chat(prompts, sampling_params=sampling_params)

    # Process results
    final_set = []
    for i, result in enumerate(results):
        for j in range(args.n_samples):
            response_text = result.outputs[j].text.strip()

            # Try to extract JSON from response (in case model adds extra text)
            try:
                # Try parsing directly
                structured_data = json.loads(response_text)
            except json.JSONDecodeError:
                # Try to extract JSON from markdown code blocks
                import re
                json_match = re.search(r'```(?:json)?\s*(\{.*?\})\s*```', response_text, re.DOTALL)
                if json_match:
                    try:
                        structured_data = json.loads(json_match.group(1))
                    except json.JSONDecodeError:
                        structured_data = None
                else:
                    # Try to find JSON object directly
                    json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
                    if json_match:
                        try:
                            structured_data = json.loads(json_match.group(0))
                        except json.JSONDecodeError:
                            structured_data = None
                    else:
                        structured_data = None

            entry = {
                'structured_cad': structured_data,
                'full_response': response_text,
                'image_path': image_files[i],
                'parse_success': structured_data is not None
            }
            final_set.append(entry)

    # Save results
    with open(args.save_path, 'w') as f:
        json.dump(final_set, f, indent=2)

    # Print statistics
    successful_parses = sum(1 for entry in final_set if entry['parse_success'])
    print(f"\n{'='*60}")
    print(f"Results saved to {args.save_path}")
    print(f"Total samples: {len(final_set)}")
    print(f"Successfully parsed JSON: {successful_parses}/{len(final_set)}")

    end_time = time.time()
    print(f"Total time: {end_time - start_time:.2f} seconds")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()

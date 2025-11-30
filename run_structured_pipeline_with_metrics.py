#!/usr/bin/env python3
"""
Wrapper script to run the structured CAD pipeline with detailed metrics tracking.

This script runs the full pipeline and tracks:
- Execution time for each step
- Throughput (samples/second)
- Success rates
- Token usage estimates

Usage:
    python run_structured_pipeline_with_metrics.py \
        --vlm_model Qwen/Qwen2.5-VL-72B-Instruct \
        --llm_model Qwen/Qwen3-Coder-30B-A3B-Instruct \
        --seed_images data/sdg_abc_1k_images \
        --tensor_parallel_size 8
"""

import subprocess
import time
import json
import argparse
from pathlib import Path
from datetime import datetime

def run_command_with_timing(cmd, description):
    """Run a command and track execution time."""
    print(f"\n{'='*80}")
    print(f"STEP: {description}")
    print(f"Command: {' '.join(cmd)}")
    print(f"{'='*80}\n")

    start_time = time.time()
    result = subprocess.run(cmd)
    end_time = time.time()

    elapsed = end_time - start_time

    if result.returncode != 0:
        print(f"\n❌ FAILED: {description}")
        return None

    print(f"\n✅ COMPLETED: {description}")
    print(f"⏱️  Time: {elapsed:.2f}s ({elapsed/60:.2f} min)")

    return {
        'description': description,
        'elapsed_seconds': elapsed,
        'elapsed_minutes': elapsed / 60,
        'timestamp': datetime.now().isoformat()
    }

def analyze_json_output(file_path, step_name):
    """Analyze JSON output and return metrics."""
    if not Path(file_path).exists():
        return None

    with open(file_path, 'r') as f:
        data = json.load(f)

    total = len(data)

    metrics = {
        'step': step_name,
        'total_samples': total
    }

    # Step-specific metrics
    if step_name == "VLM":
        successful_parses = sum(1 for item in data if item.get('parse_success', False))
        metrics['successful_json_parses'] = successful_parses
        metrics['json_parse_rate'] = successful_parses / total if total > 0 else 0

    elif step_name == "LLM":
        valid_code = sum(1 for item in data if item.get('valid_syntax') == 1)
        metrics['valid_code_samples'] = valid_code
        metrics['code_validation_rate'] = valid_code / total if total > 0 else 0

    return metrics

def main():
    parser = argparse.ArgumentParser(description='Run structured pipeline with metrics')
    parser.add_argument('--vlm_model', type=str, required=True, help='VLM model path')
    parser.add_argument('--llm_model', type=str, required=True, help='LLM model path')
    parser.add_argument('--seed_images', type=str, required=True, help='Seed images directory')
    parser.add_argument('--tensor_parallel_size', type=int, default=8, help='Tensor parallel size')
    parser.add_argument('--output_prefix', type=str, default='object_structured', help='Output file prefix')
    parser.add_argument('--skip_vlm', action='store_true', help='Skip VLM step (use existing JSON)')
    parser.add_argument('--skip_llm', action='store_true', help='Skip LLM step')
    parser.add_argument('--skip_extract', action='store_true', help='Skip file extraction')
    parser.add_argument('--skip_images', action='store_true', help='Skip image generation')

    args = parser.parse_args()

    # File paths
    vlm_output = f"{args.output_prefix}.json"
    llm_output = f"{args.output_prefix}_code.json"
    code_dir = f"generated_code_{args.output_prefix}"
    images_dir = f"generated_code_images_{args.output_prefix}"
    metrics_file = f"metrics_{args.output_prefix}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    metrics = {
        'pipeline': 'Structured CAD Pipeline',
        'timestamp': datetime.now().isoformat(),
        'configuration': {
            'vlm_model': args.vlm_model,
            'llm_model': args.llm_model,
            'seed_images': args.seed_images,
            'tensor_parallel_size': args.tensor_parallel_size
        },
        'steps': [],
        'outputs': {}
    }

    pipeline_start = time.time()

    # STEP 1: VLM
    if not args.skip_vlm:
        cmd = [
            'python3', 'inference_pipelines/runVLM_structured.py',
            '--model_path', args.vlm_model,
            '--seed_images', args.seed_images,
            '--save_path', vlm_output,
            '--tensor_parallel_size', str(args.tensor_parallel_size)
        ]

        timing = run_command_with_timing(cmd, "Step 1: VLM generates structured JSON")
        if timing:
            metrics['steps'].append(timing)

            # Analyze output
            vlm_metrics = analyze_json_output(vlm_output, "VLM")
            if vlm_metrics:
                timing['throughput_samples_per_sec'] = vlm_metrics['total_samples'] / timing['elapsed_seconds']
                timing.update(vlm_metrics)
                metrics['outputs']['vlm'] = vlm_metrics
    else:
        print(f"\n⏭️  Skipping VLM step (using existing {vlm_output})")

    # STEP 2: LLM
    if not args.skip_llm:
        cmd = [
            'python3', 'inference_pipelines/runLLM_from_structured.py',
            '--model_path', args.llm_model,
            '--seed_json_script', vlm_output,
            '--save_path', llm_output,
            '--tensor_parallel_size', str(args.tensor_parallel_size)
        ]

        timing = run_command_with_timing(cmd, "Step 2: LLM refines JSON to CadQuery code")
        if timing:
            metrics['steps'].append(timing)

            # Analyze output
            llm_metrics = analyze_json_output(llm_output, "LLM")
            if llm_metrics:
                timing['throughput_samples_per_sec'] = llm_metrics['total_samples'] / timing['elapsed_seconds']
                timing.update(llm_metrics)
                metrics['outputs']['llm'] = llm_metrics
    else:
        print(f"\n⏭️  Skipping LLM step (using existing {llm_output})")

    # STEP 3: Extract Python files
    if not args.skip_extract:
        cmd = [
            'python3', 'misc_scripts/generate_py_files.py',
            '--input_json', llm_output,
            '--output_dir', code_dir
        ]

        timing = run_command_with_timing(cmd, "Step 3: Extract Python files")
        if timing:
            metrics['steps'].append(timing)

            # Count generated files
            code_path = Path(code_dir)
            if code_path.exists():
                num_files = len(list(code_path.glob('*.py')))
                timing['files_generated'] = num_files
                timing['throughput_files_per_sec'] = num_files / timing['elapsed_seconds']
    else:
        print(f"\n⏭️  Skipping file extraction")

    # STEP 4: Generate images
    if not args.skip_images:
        cmd = [
            'python3', 'misc_scripts/generate_images.py',
            '--input_parts', code_dir,
            '--output_images', images_dir
        ]

        timing = run_command_with_timing(cmd, "Step 4: Generate images from code")
        if timing:
            metrics['steps'].append(timing)

            # Count generated images
            images_path = Path(images_dir)
            if images_path.exists():
                num_images = len(list(images_path.glob('*.png')))
                timing['images_generated'] = num_images
                timing['throughput_images_per_sec'] = num_images / timing['elapsed_seconds']
    else:
        print(f"\n⏭️  Skipping image generation")

    pipeline_end = time.time()

    # Calculate total metrics
    metrics['total_elapsed_seconds'] = pipeline_end - pipeline_start
    metrics['total_elapsed_minutes'] = (pipeline_end - pipeline_start) / 60
    metrics['total_elapsed_hours'] = (pipeline_end - pipeline_start) / 3600

    # Save metrics
    with open(metrics_file, 'w') as f:
        json.dump(metrics, f, indent=2)

    # Print summary
    print(f"\n{'='*80}")
    print(f"{'='*80}")
    print(f"PIPELINE COMPLETE!")
    print(f"{'='*80}")
    print(f"{'='*80}\n")

    print("📊 SUMMARY METRICS\n")

    for step in metrics['steps']:
        print(f"  {step['description']}:")
        print(f"    ⏱️  Time: {step['elapsed_seconds']:.2f}s ({step['elapsed_minutes']:.2f} min)")

        if 'throughput_samples_per_sec' in step:
            print(f"    🚀 Throughput: {step['throughput_samples_per_sec']:.2f} samples/sec")

        if 'json_parse_rate' in step:
            print(f"    ✅ JSON Parse Rate: {step['json_parse_rate']*100:.1f}%")
            print(f"    📝 Successful Parses: {step['successful_json_parses']}/{step['total_samples']}")

        if 'code_validation_rate' in step:
            print(f"    ✅ Code Validation Rate: {step['code_validation_rate']*100:.1f}%")
            print(f"    ✓  Valid Code: {step['valid_code_samples']}/{step['total_samples']}")

        if 'files_generated' in step:
            print(f"    📁 Files Generated: {step['files_generated']}")

        if 'images_generated' in step:
            print(f"    🖼️  Images Generated: {step['images_generated']}")

        print()

    print(f"⏱️  Total Pipeline Time: {metrics['total_elapsed_seconds']:.2f}s ({metrics['total_elapsed_minutes']:.2f} min / {metrics['total_elapsed_hours']:.2f} hrs)")
    print(f"\n📊 Detailed metrics saved to: {metrics_file}")
    print(f"\n{'='*80}\n")

if __name__ == '__main__':
    main()

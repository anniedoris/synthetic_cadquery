#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=80G
#SBATCH -p pi_faez
#SBATCH --gres=gpu:2
#SBATCH --time=4-00:00:00
#SBATCH -J cadquery_pipeline
#SBATCH -o /orcd/home/002/erasyla/synthetic_cadquery/pipeline_%j.out
#SBATCH -e /orcd/home/002/erasyla/synthetic_cadquery/pipeline_%j.err
#SBATCH -D /orcd/home/002/erasyla/synthetic_cadquery

# Load required modules
module load deprecated-modules
module load anaconda3/2022.05-x86_64
module load cuda/12.4.0

# Activate conda environment
source ~/.bashrc
conda activate vllm_env

# Verify CUDA
echo "CUDA available:"
python -c "import torch; print(torch.cuda.is_available())"
echo "GPU count:"
python -c "import torch; print(torch.cuda.device_count())"

# Run the pipeline with 2 GPUs
python3 run_structured_pipeline_with_metrics.py \
    --vlm_model Qwen/Qwen2.5-VL-72B-Instruct \
    --llm_model Qwen/Qwen3-Coder-30B-A3B-Instruct \
    --seed_images data/sdg_abc_1k_images \
    --tensor_parallel_size 2 \
    --skip_images

echo "Pipeline completed!"

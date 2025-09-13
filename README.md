## Overview

VLM-LLM pipeline to generate synthetic CadQuery code conditioned on images of objects.

So far, have tested the pipeline using 1000 images of CAD objects from the ABC dataset. You can find these images in ```data/sdg_abc_1k_images```.

## Running VLM Portion of the Pipeline

To run as I did, use:

```
python inference_pipelines/runVLM.py --model_path Qwen/Qwen2.5-VL-72B-Instruct --seed_images data/sdg_abc_1k_images --save_path object_descriptions.json
```

Note: this will overwrite currently existing ```object_descriptions.json``` file.

## Running LLM Portion of the Pipeline

To then pass the generated descriptions to an LLM to generate CadQuery code, use:

```
python inference_pipelines/runLLM.py --model_path Qwen/Qwen3-Coder-30B-A3B-Instruct --seed_json_script object_descriptions.json --save_path sdg.json
```

Note: to get Qwen3-Coder running with vllm, I had to use an older version (0.8.4) versus 0.9.1 which I usually use.

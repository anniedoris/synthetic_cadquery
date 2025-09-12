## Overview

VLM-LLM pipeline to generate synthetic CadQuery code conditioned on images of objects.

So far, have tested the pipeline using 1000 images of CAD objects from the ABC dataset. You can find these images in ```data/sdg_abc_1k_images```.

## Running VLM Portion of the Pipeline

To run as I did, use:

```
python inference_pipelines/runVLM.py --model_path Qwen/Qwen2.5-VL-72B-Instruct --seed_images data/sdg_abc_1k_images --save_path object_descriptions.json
```

Note: this will overwrite currently existing ```object_descriptions.json``` file.
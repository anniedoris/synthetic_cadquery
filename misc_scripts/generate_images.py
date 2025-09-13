import os
import argparse
from PartToImage import convert_part_to_image
import shutil
from tqdm import tqdm

def get_cad_paths(root_dir):
    model_paths = []
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.lower().endswith(('.step', '.obj', '.py')):
                full_path = os.path.join(dirpath, filename)
                rel_path = os.path.relpath(full_path, root_dir)
                model_paths.append(rel_path)
    return model_paths

def main():
    parser = argparse.ArgumentParser(description="Render 3D parts to image files.")
    parser.add_argument("--input_parts", type=str, required=True, help="Path to folder of .obj or .step files or .py files.")
    parser.add_argument("--output_images", type=str, required=True, help="Path to save output image files.")
    args = parser.parse_args()

    # if os.path.exists(args.output_images):
    #     shutil.rmtree(args.output_images)
    #     print(f"Deleted existing folder: {args.output_images}")
    os.makedirs(args.output_images, exist_ok=True)
    print(f"Created folder: {args.output_images}")

    # Get CAD paths
    print(f"Input path: {args.input_parts}")
    all_cad_files = get_cad_paths(args.input_parts)
    print("All CAD Files")
    print(all_cad_files)

    for file in tqdm(all_cad_files):

        input_path = os.path.join(args.input_parts, file)
        png_name = os.path.splitext(file)[0] + ".png"
        png_name = png_name.replace("/", "_")
        output_path = os.path.join(args.output_images, png_name)
        
        # print(output_path)
        try:
            convert_part_to_image(f"{input_path}", "iso", f"{output_path}", "BRepName", remove_bg=True)
        except Exception as e:
            print(e)
            continue

if __name__ == "__main__":
    main()
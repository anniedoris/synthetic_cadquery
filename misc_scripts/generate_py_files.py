#!/usr/bin/env python3
"""
Script to generate Python files from JSON data.

Usage:
    python generate_py_files.py --input_json sdg.json --output_dir generated_code

This script reads a JSON file containing code entries and extracts only those
with valid_syntax=1, saving the code content to individual .py files.
"""

import json
import os
import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description='Generate Python files from JSON data')
    parser.add_argument('--input_json', required=True, help='Path to input JSON file')
    parser.add_argument('--output_dir', required=True, help='Output directory for generated Python files')
    
    args = parser.parse_args()
    
    # Read the JSON file
    try:
        with open(args.input_json, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: Input file '{args.input_json}' not found.")
        return 1
    
    # Create output directory if it doesn't exist
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Process entries and generate files
    valid_count = 0
    total_count = len(data)
    
    for i, entry in enumerate(data):
        # Check if the entry has valid syntax
        if entry.get('valid_syntax') == 1:
            code_content = entry.get('code', '')
            
            if code_content:
                # Generate filename based on index and image path if available
                image_path = entry.get('image_path', '')
                if image_path:
                    # Extract filename from image path and replace extension
                    base_name = Path(image_path).stem
                    filename = f"{base_name}.py"
                else:
                    # Fallback to index-based naming
                    filename = f"generated_code_{i:05d}.py"
                
                output_file = output_dir / filename
                
                # Write the code to file
                try:
                    with open(output_file, 'w', encoding='utf-8') as f:
                        f.write(code_content)
                    print(f"Generated: {output_file}")
                    valid_count += 1
                except IOError as e:
                    print(f"Error writing file '{output_file}': {e}")
            else:
                print(f"Warning: Entry {i} has valid_syntax=1 but no code content")
    
    print(f"\nSummary:")
    print(f"Total entries processed: {total_count}")
    print(f"Valid entries (valid_syntax=1): {valid_count}")
    print(f"Python files generated: {valid_count}")
    print(f"Output directory: {output_dir.absolute()}")
    
    return 0


if __name__ == '__main__':
    exit(main())

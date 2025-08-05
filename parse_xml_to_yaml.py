import argparse
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(__file__, '..', '..')))

import parse_xml.parse_xml as driver
import yaml

def parse_and_store_results(input_path, output_path):
    # Determine if input is a folder or a single file
    is_dir = os.path.isdir(input_path)
    is_file = os.path.isfile(input_path) and input_path.lower().endswith('.xml')
    if not is_dir and not is_file:
        raise FileNotFoundError(f"Input path '{input_path}' does not exist or is not an .xml file")

    # If input is a directory, ensure output is treated as a directory
    if is_dir:
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        xml_files = [f for f in os.listdir(input_path) if f.lower().endswith('.xml')]
        if not xml_files:
            print(f"No .xml files found in directory '{input_path}'.")
            return

        for file in xml_files:
            source_file_path = os.path.join(input_path, file)
            print(f"Processing file {file}...")
            result = driver.parse_shortcut_xml(source_file_path)
            result_str = format_result(result)

            # Name the output .txt file after the XML (same basename)
            base = os.path.splitext(file)[0]
            txt_file_name = base + '.txt'
            result_file_path = os.path.join(output_path, txt_file_name)

            if os.path.exists(result_file_path):
                print(f"File {txt_file_name} already exists. Skipping...")
                continue

            try:
                with open(result_file_path, 'w', encoding='utf-8') as result_file:
                    # Dump as YAML string (actions part)
                    yaml.safe_dump(result_str, result_file, default_flow_style=False, allow_unicode=True)
            except Exception as e:
                print(f"Error writing '{txt_file_name}':")
                print(result_str)
                raise

        print(f"Processed {len(xml_files)} files. Results are stored in '{output_path}'.")

    else:
        # Single-file case: output_path should be a file (or a directory where we put one file)
        # If output_path exists and is a directory, write into that directory
        # Otherwise, treat output_path as a file path.
        xml_file = os.path.basename(input_path)
        print(f"Processing single file {xml_file}...")
        result = driver.parse_shortcut_xml(input_path)
        result_str = format_result(result)

        # Determine final output file path
        if os.path.isdir(output_path):
            # Write into this directory, naming after the single XML
            base = os.path.splitext(xml_file)[0]
            txt_file_name = base + '.txt'
            result_file_path = os.path.join(output_path, txt_file_name)
        else:
            # Treat output_path as the target file (ensure it ends with .txt)
            if output_path.lower().endswith('.txt'):
                result_file_path = output_path
            else:
                # If no .txt extension given, append .txt
                result_file_path = output_path + '.txt'

            # Ensure the parent directory exists
            parent_dir = os.path.dirname(result_file_path)
            if parent_dir and not os.path.exists(parent_dir):
                os.makedirs(parent_dir)

        if os.path.exists(result_file_path):
            print(f"File '{result_file_path}' already exists. Overwriting...")
        try:
            with open(result_file_path, 'w', encoding='utf-8') as result_file:
                yaml.safe_dump(result_str, result_file, default_flow_style=False, allow_unicode=True)
        except Exception as e:
            print(f"Error writing '{result_file_path}':")
            print(result_str)
            raise

        print(f"Processed '{xml_file}'. Result is stored in '{result_file_path}'.")


def format_result(result):
    """Format the tuple (metadata, trigger, actions, output) into a string."""
    metadata, trigger, actions, output = result
    return actions


def main():
    parser = argparse.ArgumentParser(
        description="Parse Apple Shortcuts .xml file(s) to YAML")
    parser.add_argument(
        "input",
        help="Path to an .xml file OR a directory containing .xml files")
    parser.add_argument(
        "-o", "--output", dest="output", default="./test_shareshortcut_result_yaml",
        help="Directory or file in which YAML results will be placed (default: %(default)s)")
    args = parser.parse_args()
    parse_and_store_results(args.input, args.output)


if __name__ == "__main__":
    main()

import os
import time

import calculate_result_of_folder
import code_filter
import parse_icloud_link as parse_icloud_link
import parse_xml_to_yaml as parse_xml_to_yaml

def main(link, type='single'):
    file_or_folder_name = ""
    if type == 'single':
        # Process a single iCloud link
        generated_xml = parse_icloud_link.run(link)
        file_or_folder_name = generated_xml
        print(f"Generated XML for single link: {generated_xml}")
        # Process XML to YAML
        # parse_xml_to_yaml.parse_and_store_results(generated_xml, )
    else:
        timestamp = int(time.time())
        folder_name = f"shortcuts_xml_batch_{timestamp}"
        os.makedirs(folder_name, exist_ok=True)

        all_xml_files = []
        for i, item in enumerate(link):
            # Process each iCloud link in the list
            generated_xml = parse_icloud_link.run(item, output_dir=folder_name)
            all_xml_files.append(generated_xml)
            print(f"Generated XML for link {i + 1}/{len(link)} ({item}): {generated_xml}")

        print(f"All XML files saved to folder: {folder_name}")
        file_or_folder_name = folder_name
    yaml_output_dir = ""
    if type == 'single':
        # For single file: remove .xml extension and add _yamls
        base_name = os.path.splitext(file_or_folder_name)[0]
        yaml_output_dir = f"{base_name}_yamls"
    else:
        # For batch: replace xml with yaml in folder name
        yaml_output_dir = file_or_folder_name.replace('xml', 'yaml')
    # Process all XML files to YAML
    parse_xml_to_yaml.parse_and_store_results(file_or_folder_name, yaml_output_dir)

    # Code filter to separate safe and unsafe YAMLs based on their actions
    print("Running security analysis on generated YAML files...")

    # Create analysis output directory
    timestamp = int(time.time())
    analysis_output_dir = ""

    if type == 'single':
        # For single file analysis
        # Create output file path for analysis results
        base_name = os.path.splitext(yaml_output_dir)[0]
        input_file = f"{base_name}.txt"
        analysis_output_dir = f"{base_name}_analysis_{timestamp}.txt"
        code_filter.code_analysis(input_file, analysis_output_dir, debug=True)
        print(f"Security analysis completed: {analysis_output_dir}")
    else:
        # For batch processing
        analysis_output_dir = f"{yaml_output_dir}_analysis_{timestamp}"
        os.makedirs(analysis_output_dir, exist_ok=True)
        code_filter.run_all(debug=True, input_folder_path=yaml_output_dir, output_folder_path=analysis_output_dir)
        print(f"Batch security analysis completed: {analysis_output_dir}")

    # Run calculate result of categories
    result_category_path = f"{file_or_folder_name}_result_categories_{timestamp}"
    if type == 'single':
        calculate_result_of_folder.process_path(analysis_output_dir, f"{result_category_path}.txt")
    else:
        calculate_result_of_folder.process_path(analysis_output_dir, result_category_path)

    # At this point, if all attack are shown as False, then we do not need to run the LLM.
    # If you need to run the LLM, there are two options:
    # 1. Run the LLM through API, in this case, we do not filter the token length as we do not know what kind of API you are using -- we will provide an example one.

    # 2. Run a local LLM, in this case, we provide an example of filtering the token length, and using Qwen-32B-Instruct-Coder to analyze the results.


if __name__ == "__main__":
    main('https://www.icloud.com/shortcuts/0854ca93a7fd4d1bbd44a2f895e1b4b2', type='single')
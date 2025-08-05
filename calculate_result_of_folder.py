import argparse
import os
import pandas as pd
from collections import defaultdict
import re

def sanitize_filename(name):
    """
    Sanitize the action category name to create a valid filename.
    Removes or replaces characters that are invalid in filenames.
    """
    # Replace spaces with underscores
    name = name.replace(' ', '_')
    # Remove any characters that are not alphanumeric, underscores, or hyphens
    name = re.sub(r'[^\w\-]', '', name)
    return name

def process_path(input_path, output_path):
    """
    Processes either a single file or an entire folder, counting action categories
    and writing lists of files per action category into separate files.

    - If input_path is a directory: iterates over all files inside.
    - If input_path is a single file: processes only that file.

    Returns:
    - action_counts_df: DataFrame of counts of True/False for each action category.
    - all_false_files: Integer count of files where all actions are False.
    """
    # Determine if input_path is a directory or a file
    is_dir = os.path.isdir(input_path)
    is_file = os.path.isfile(input_path) and input_path.lower().endswith('.txt') or input_path.lower().endswith('.xml')  # :contentReference[oaicite:9]{index=9}

    if not is_dir and not is_file:
        raise FileNotFoundError(f"Input path '{input_path}' does not exist or is not a valid file/folder")

    # If it’s a directory, ensure output_path is treated as a folder
    if is_dir:
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        # Prepare subfolder for per-category file lists
        action_output_dir = os.path.join(output_path, "action_categories")
        if not os.path.exists(action_output_dir):
            os.makedirs(action_output_dir)

        # Collect all files in the directory
        all_files = [f for f in os.listdir(input_path) if os.path.isfile(os.path.join(input_path, f))]
        # Call the helper to process multiple files
        return _process_multiple_files(input_path, all_files, output_path, action_output_dir)

    else:
        # Single-file case: prepare to write exactly one output file
        if os.path.isdir(output_path):
            # If output_path is an existing directory, write basename(input).txt inside it
            base = os.path.splitext(os.path.basename(input_path))[0]
            result_file_name = base + '.txt'
            result_file_path = os.path.join(output_path, result_file_name)
        else:
            # If output_path is intended as a filename, ensure it ends with .txt
            if output_path.lower().endswith('.txt'):
                result_file_path = output_path
            else:
                result_file_path = output_path + '.txt'

            parent_dir = os.path.dirname(result_file_path)
            if parent_dir and not os.path.exists(parent_dir):
                os.makedirs(parent_dir)

        # Process only the single file
        return _process_single_file(input_path, result_file_path)

def _process_multiple_files(input_folder, file_list, output_folder, action_output_dir):
    """
    Internal helper: processes a list of filenames in the input_folder,
    writes per-category file lists under action_output_dir, and a CSV of counts.
    """
    action_counts = {}
    all_false_files_count = 0
    all_false_files_names = []
    action_files = defaultdict(set)  # Map category → set of filenames

    for fname in file_list:
        file_path = os.path.join(input_folder, fname)
        all_false = True

        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                if ": " in line:
                    key, value = line.strip().split(": ", 1)
                    value = value.strip()

                    # Initialize counts if needed
                    if key not in action_counts:
                        action_counts[key] = {'False': 0, 'True': 0}
                    # Increment count
                    if value in action_counts[key]:
                        action_counts[key][value] += 1
                    else:
                        action_counts[key][value] = 1

                    if value == "True":
                        all_false = False
                        action_files[key].add(fname)

        if all_false:
            all_false_files_count += 1
            all_false_files_names.append(fname)

    # Build DataFrame of counts
    action_counts_df = pd.DataFrame(action_counts).T
    # Reorder columns if both exist
    if 'False' in action_counts_df.columns and 'True' in action_counts_df.columns:
        action_counts_df = action_counts_df[['False', 'True']]
        action_counts_df.columns = ["False Count", "True Count"]
    action_counts_df.index.name = "Action Category"

    # Print summary
    print("Action Counts:")
    print(action_counts_df)
    print(f"\nNumber of files where all actions are False: {all_false_files_count}")

    # Write counts CSV
    action_counts_csv_path = os.path.join(output_folder, "action_counts.csv")
    action_counts_df.to_csv(action_counts_csv_path, encoding='utf-8')
    print(f"Action counts saved to {action_counts_csv_path}")

    # For each category, write the filenames that had True
    for category, fileset in action_files.items():
        sanitized = sanitize_filename(category)
        out_path = os.path.join(action_output_dir, f"{sanitized}.txt")
        with open(out_path, 'w', encoding='utf-8') as af:
            for fn in sorted(fileset):
                af.write(f"{fn}\n")
        print(f"Files for action category '{category}' written to {out_path}")

    # Write the names of all-false files
    all_false_path = os.path.join(output_folder, "all_false_files.txt")
    with open(all_false_path, 'w', encoding='utf-8') as afc:
        for fn in all_false_files_names:
            afc.write(f"{fn}\n")
    print(f"All-false filenames written to {all_false_path}")

    return action_counts_df, all_false_files_count

def _process_single_file(input_file, result_file_path):
    """
    Internal helper: processes a single file, writes results to one output .txt file.
    Returns a dummy DataFrame and count (to match signature).
    """
    action_counts = {}
    all_false = True
    action_files = defaultdict(set)

    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            if ": " in line:
                key, value = line.strip().split(": ", 1)
                value = value.strip()

                if key not in action_counts:
                    action_counts[key] = {'False': 0, 'True': 0}
                if value in action_counts[key]:
                    action_counts[key][value] += 1
                else:
                    action_counts[key][value] = 1

                if value == "True":
                    all_false = False
                    action_files[key].add(os.path.basename(input_file))

    # Build and print a minimal summary for single file
    action_counts_df = pd.DataFrame(action_counts).T
    if 'False' in action_counts_df.columns and 'True' in action_counts_df.columns:
        action_counts_df = action_counts_df[['False', 'True']]
        action_counts_df.columns = ["False Count", "True Count"]
    action_counts_df.index.name = "Action Category"

    print("Action Counts for single file:")
    print(action_counts_df)
    if all_false:
        print("All actions were False in this file.")
    else:
        print("At least one action was True in this file.")

    # Write the entire result (e.g., combined action counts) into result_file_path
    with open(result_file_path, 'w', encoding='utf-8') as rf:
        yaml_content = action_counts_df.to_csv()  # Or any desired formatting; here using CSV as example
        rf.write(yaml_content)
    print(f"Single-file result written to {result_file_path}")

    # Return for consistency (though counts from one file may be less useful)
    return action_counts_df, (1 if all_false else 0)

def main():
    parser = argparse.ArgumentParser(description="Process files (or a single file) and generate action counts.")
    parser.add_argument('--input', required=True,
                        help='Path to an input folder or a single file to process.')
    parser.add_argument('--output', required=True,
                        help='Path to the output folder (for multiple files) or output file (for single file).')
    args = parser.parse_args()

    input_path = args.input
    output_path = args.output

    process_path(input_path, output_path)

if __name__ == "__main__":
    main()

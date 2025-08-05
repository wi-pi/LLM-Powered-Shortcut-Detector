import csv
from collections import defaultdict


def analyze_action_data(csv_file_path, action_name=''):
    # Initialize a dictionary to store the counts for each category
    categories_count = {
        "Data Collection": 0,
        "Data Insertion": 0,
        "Data Exfiltration": 0,
        "Resource Control": 0,
        "Trace Hiding": 0
    }

    return_list = []

    # Open the CSV file and read data
    with open(csv_file_path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        # Iterate over each row in the CSV file
        for row in csv_reader:
            # Check each category for a value, increment the count if there's a value
            for category in categories_count.keys():
                if row[category]:  # Non-empty field
                    categories_count[category] += 1
                    if category == action_name:
                        # Remove double quotes from the description if present
                        description = row['Prompt Description'].strip('\'')
                        return_list.append(description)

    print(return_list)
    return categories_count

# print(analyze_action_data('combined_actions_annotated.csv', 'Trace Hiding'))

import pandas as pd


# Define the function to process the CSV
def process_csv(input_file, output_file):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(input_file)

    # Filter rows where 'Data Exfiltration' column has value 1
    filtered_df = df[df['Data Exfiltration'] == 1]

    # Keep only 'Action Name' and 'Prompt Description' columns
    filtered_df = filtered_df[['Action Name', 'Prompt Description']]

    # Append two new columns: 'to victim' and 'to others'
    filtered_df['to victim'] = None  # You can initialize these with default values or keep them blank
    filtered_df['to others'] = None

    # Save the new DataFrame to a CSV file
    filtered_df.to_csv(output_file, index=False)


# Example usage
input_csv = 'combined_actions_annotated.csv'  # Replace with your input file path
output_csv = 'recipient_annotation_new.csv'  # Replace with your desired output file path

# process_csv(input_csv, output_csv)

def interpret_annotated_csv(file_path):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    df['Prompt Description'] = df['Prompt Description'].str.strip("'")

    # Count the rows where 'to victim' is marked 1 but 'to others' is not
    victim_only_count = len(df[(df['to victim'] == 1) & (df['to others'].isna())])

    # Create lists for "only victim marked" and "only others marked"
    only_victim_marked = df[(df['to victim'] == 1) & (df['to others'].isna())]['Prompt Description'].tolist()
    only_others_marked = df[(df['to others'] == 1)]['Prompt Description'].tolist()

    for item in only_others_marked:
        if item in only_victim_marked:
            only_others_marked.pop(item)

    # Print the results
    print(f"Number of actions marked only as victim: {victim_only_count}")
    print("Actions marked only as victim:", only_victim_marked)
    print("Actions marked only as others:", only_others_marked)


# Example usage
annotated_csv = 'recipient_annotation_new.csv'  # Replace with your annotated CSV file path
# interpret_annotated_csv(annotated_csv)


# # Process the data by splitting lines and parsing
# processed_data = []
# for line in data.strip().split("\n"):
#     # Check for lines with the expected format
#     if "': " in line:
#         cleaned_line = line.strip().strip(",")  # Remove any trailing commas
#         # Split by `': ` and strip quotes only from the first column
#         split_line = [cleaned_line.split("': ")[0].strip("'"), cleaned_line.split("': ")[1]]
#         if len(split_line) == 2:  # Ensure it splits into exactly two parts
#             processed_data.append(split_line)
#
# # Create a DataFrame
# df = pd.DataFrame(processed_data, columns=["Action", "Function"])
#
# # Save the DataFrame as a CSV file
# file_path = "shortcuts_function_full.csv"
# # df.to_csv(file_path, index=False)

# print(f"CSV saved to: {file_path}")

def process_files(file_paths):
    if len(file_paths) != 4:
        raise ValueError("Exactly 4 file paths must be provided.")

    all_names = set()
    duplicate_count = 0

    for file_path in file_paths:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                initial_size = len(all_names)
                all_names.update(line.strip() for line in lines)
                duplicate_count += len(lines) - (len(all_names) - initial_size)
        except Exception as e:
            print(f"Error processing file {file_path}: {e}")

    return len(all_names), duplicate_count

def process_files_without_duplicates(file_paths):
    total_names = 0

    for file_path in file_paths:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                total_names += len(lines)
        except Exception as e:
            print(f"Error processing file {file_path}: {e}")

    return total_names

def count_responses(file_paths, default_response_prefix="Maybe"):
    yes_count = 0
    no_count = 0
    maybe_count = 0

    for file_path in file_paths:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    response = row.get("Response", "").strip()
                    if response.startswith(default_response_prefix):
                        maybe_count += 1
                    elif response == "Yes":
                        yes_count += 1
                    elif response == "No":
                        no_count += 1
        except Exception as e:
            print(f"Error processing file {file_path}: {e}")

    return yes_count, no_count, maybe_count

def count_unique_yes_and_no_shortcuts(domain_file_groups):
    """
    Takes 16 CSVs from 4 attack operations across 4 domains,
    and returns the total number of unique shortcuts with 'Yes' and 'No' in each domain.

    Args:
        domain_file_groups (dict): A dictionary where keys are domain names and
                                   values are lists of file paths for the domain.

    Returns:
        dict: A dictionary with domain names as keys and dictionaries with the counts of
              unique 'Yes' and 'No' shortcuts as values.
    """
    domain_results = {}

    for domain, file_paths in domain_file_groups.items():
        shortcut_responses = defaultdict(list)

        # Aggregate responses for each shortcut across files
        for file_path in file_paths:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        response = row.get("Response", "").strip()
                        shortcut = row.get("Input File", "").strip()

                        if shortcut:
                            shortcut_responses[shortcut].append(response)
            except Exception as e:
                print(f"Error processing file {file_path}: {e}")

        # Determine unique 'Yes' and 'No' shortcuts
        unique_yes = set()
        unique_no = set()

        for shortcut, responses in shortcut_responses.items():
            if any(r.startswith("Yes") for r in responses):
                unique_yes.add(shortcut)
            if all(r == "No" for r in responses) and len(responses) == len(file_paths):
                unique_no.add(shortcut)

        # Store results for the domain
        domain_results[domain] = {
            "Total Unique 'Yes'": len(unique_yes),
            "Total Unique 'No'": len(unique_no),
        }

    return domain_results


import os


def record_filenames(folder_path, output_file="filenames.txt"):
    try:
        # Check if the folder exists
        if not os.path.isdir(folder_path):
            print(f"The folder '{folder_path}' does not exist.")
            return

        # Get all files in the folder
        files = os.listdir(folder_path)

        # Filter out only files (exclude directories)
        filenames = [os.path.splitext(file)[0] for file in files if os.path.isfile(os.path.join(folder_path, file))]

        # Write filenames to the output file with UTF-8 encoding
        with open(output_file, "w", encoding="utf-8") as file:
            file.write("\n".join(filenames))

        print(f"Filenames have been recorded in '{output_file}'.")
    except Exception as e:
        print(f"An error occurred: {e}")




if __name__ == "__main__":
    # file_paths = ['../test/output_results/action_categories/Impersonation.txt_unsafe.txt', '../test/output_results/action_categories/Lockout_Control.txt_unsafe.txt', '../test/output_results/action_categories/Overload.txt_unsafe.txt', '../test/output_results/action_categories/SpywareStalkerware_Data_Exfiltration.txt_unsafe.txt']
    # #
    # total_unique, total_duplicates = process_files(file_paths)
    # #
    # print(f"Total unique names: {total_unique}")
    # print(f"Total duplicate names: {total_duplicates}")
    # file_paths = ['../test/output_results/action_categories/SpywareStalkerware_Data_Exfiltration.txt_safe.txt', '../test/output_results_routinehub/action_categories/SpywareStalkerware_Data_Exfiltration.txt_safe.txt', '../test/output_results_matt/action_categories/SpywareStalkerware_Data_Exfiltration.txt_safe.txt', '../test/output_results_shareshortcut/action_categories/SpywareStalkerware_Data_Exfiltration.txt_safe.txt']
    #
    # total_names = process_files_without_duplicates(file_paths)
    # print(f"Total names: {total_names}")
    # file_path = ['../llm/overload_routinehub_test_set_result.csv', '../llm/overload_matt_test_set_result.csv', '../llm/overload_share_test_set_result.csv', '../llm/overload_main_test_set_result.csv']
    # file_path = ['../llm/lockout_routinehub_test_set_result.csv', '../llm/lockout_matt_test_set_result.csv', '../llm/lockout_share_test_set_result.csv', '../llm/lockout_main_test_set_result.csv']
    # file_path = ['../llm/spy_routinehub_test_set_result.csv', '../llm/spy_matt_test_set_result.csv', '../llm/spy_share_test_set_result.csv', '../llm/spy_main_test_set_result.csv']
    # file_path = ['../llm/impersonation_routinehub_test_set_result.csv', '../llm/impersonation_matt_test_set_result.csv', '../llm/impersonation_share_test_set_result.csv', '../llm/impersonation_main_test_set_result.csv']
    #
    # yes_count, no_count, maybe_count = count_responses(file_path)
    # print(f"Yes count: {yes_count}")
    # print(f"No count: {no_count}")
    # print(f"Maybe count: {maybe_count}")
    domain_file_groups = {
        "routinehub": ['../llm/overload_routinehub_test_set_result.csv', '../llm/lockout_routinehub_test_set_result.csv', '../llm/spy_routinehub_test_set_result.csv', '../llm/impersonation_routinehub_test_set_result.csv'],
        "matt": ['../llm/overload_matt_test_set_result.csv', '../llm/lockout_matt_test_set_result.csv', '../llm/spy_matt_test_set_result.csv', '../llm/impersonation_matt_test_set_result.csv'],
        "share": ['../llm/overload_share_test_set_result.csv', '../llm/lockout_share_test_set_result.csv', '../llm/spy_share_test_set_result.csv', '../llm/impersonation_share_test_set_result.csv'],
        "gallery": ['../llm/overload_main_test_set_result.csv', '../llm/lockout_main_test_set_result.csv', '../llm/spy_main_test_set_result.csv', '../llm/impersonation_main_test_set_result.csv'],
    }

    unique_yes_counts = count_unique_yes_and_no_shortcuts(domain_file_groups)

    for domain, count in unique_yes_counts.items():
        print(f"Total unique shortcuts with 'Yes' in {domain}: {count}")

    # Example usage
    # folder_path = "../test/test_shareshortcut_result_yaml"
    # record_filenames(folder_path)

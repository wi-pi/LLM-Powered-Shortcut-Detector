# File path of the input and output
import pandas as pd
import csv

def txt_to_csv(input_file_path, output_file_path):
    # Read and parse the input file
    actions = []
    with open(input_file_path, 'r') as file:
        for line in file:
            if line.strip():  # Skip empty lines
                parts = line.split(':')
                action_name = parts[0].strip().strip("'")
                action_function = parts[1].strip().rstrip(',')  # Remove trailing commas
                actions.append((action_name, action_function))

    # Sort the parsed data, placing all 'action_external_app' items at the end
    actions_sorted = sorted(
        actions,
        key=lambda x: (x[1] == 'action_external_app', x[1])
    )

    with open(output_file_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Action Name', 'Action Function'])  # Header
        writer.writerows(actions_sorted)

    print(f"CSV file has been created at {output_file_path}")

input_file_path = 'action_list.txt'
output_file_path = 'parsed_actions.csv'
# txt_to_csv(input_file_path, output_file_path)

def append_descriptions(input_txt_path, csv_input_path, csv_output_path):
    # Read the descriptions from the input text file
    descriptions = {}
    with open(input_txt_path, 'r') as file:
        for line in file:
            if line.strip():  # Skip empty lines
                parts = line.split(':', 1)  # Limit split to 1 to avoid splitting further parts
                if len(parts) == 2:  # Ensure there are at least 2 parts after splitting
                    action_name = parts[0].strip().strip("'")  # Remove single quotes around action name
                    description = parts[1].strip().rstrip(',')  # Keep single quotes around description
                    descriptions[action_name] = description
                else:
                    print(f"Skipping invalid line: {line}")

    # Read the CSV into a DataFrame
    df = pd.read_csv(csv_input_path)

    # Create a new column for prompt.txt descriptions and fill it based on matches
    df['Prompt Description'] = df['Action Name'].map(descriptions)

    # Find unmatched action names
    unmatched_actions = df[df['Prompt Description'].isna()]['Action Name'].tolist()

    # Save the updated DataFrame to a new CSV file
    df.to_csv(csv_output_path, index=False)

    print(f"CSV file has been updated and saved to {csv_output_path}")
    if unmatched_actions:
        print("Unmatched action names:")
        for action in unmatched_actions:
            print(action)
    else:
        print("All actions were matched successfully.")

# append_descriptions('action_to_prompt.txt', 'parsed_actions.csv', 'updated_parsed_actions.csv')



def combine_csv_keep_both(file_a, file_b, output_file):
    """
    Combines two CSV files by matching their first columns and keeps data from both files.
    The output will contain three columns: Action, Description_A, Description_B.

    Parameters:
        file_a (str): Path to the first CSV file.
        file_b (str): Path to the second CSV file.
        output_file (str): Path to save the combined CSV.

    Returns:
        None: Saves the combined CSV to `output_file`.
    """
    # Load the CSVs
    df_a = pd.read_csv(file_a)
    df_b = pd.read_csv(file_b)

    # Rename columns to indicate which file they come from
    df_a.columns = ["Action Name", "Description"]
    df_b.columns = ["Action Name", "Action Function"]

    # Merge the DataFrames on the first column, keeping all matches
    combined_df = pd.merge(df_a, df_b, on="Action Name", how="inner")

    # Save the result to the output file
    combined_df.to_csv(output_file, index=False)
    print(f"Combined CSV saved to: {output_file}")


# combine_csv_keep_both('shortcuts_actions_full.csv', 'shortcuts_function_full.csv', 'combined_actions.csv')


def combine_and_annotate(csv_a, csv_b, output_file):
    """
    Combines two CSV files based on the first column, keeps all data from CSV A,
    appends additional columns from CSV B, and prints lines missing in CSV B
    where 'Action Function' is not 'action_external_app'.

    Parameters:
        csv_a (str): Path to the first CSV file (CSV A).
        csv_b (str): Path to the second CSV file (CSV B).
        output_file (str): Path to save the combined CSV file.

    Returns:
        None: Saves the combined CSV to the specified output file.
    """
    # Load both CSV files
    df_a = pd.read_csv(csv_a)
    df_b = pd.read_csv(csv_b)

    # Filter missing lines in CSV B where 'Action Function' is not 'action_external_app'
    df_missing = df_a[~df_a['Action Name'].isin(df_b['Action Name'])]
    missing_non_external = df_missing[df_missing['Action Function'] != 'action_external_app']

    # Print the missing lines
    print("Missing lines in CSV B where 'Action Function' is not 'action_external_app':")
    print(missing_non_external)

    # Merge CSV A and CSV B based on 'Action Name', keeping all data from CSV A
    combined_df = pd.merge(df_a, df_b, on='Action Name', how='left')

    # Ensure columns from CSV B are appended correctly
    columns_to_append = ['Data Collection', 'Data Insertion', 'Data Exfiltration', 'Resource Control', 'Trace Hiding']
    for col in columns_to_append:
        if col not in combined_df.columns:
            combined_df[col] = None

    # Save the combined data to the output file
    combined_df.to_csv(output_file, index=False)
    print(f"Combined CSV saved to: {output_file}")

combine_and_annotate('combined_actions.csv', 'updated_parsed_actions.csv', 'combined_actions_annotated.csv')


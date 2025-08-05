import os
import time

import yaml

import calculate_result_of_folder
import code_filter
import parse_icloud_link as parse_icloud_link
import parse_xml_to_yaml as parse_xml_to_yaml
from groq import Groq


def run_multiple_rounds(shortcut_text, scenario):
    """
    Calls the Groq LLM for multiple rounds for a given scenario,
    referencing local prompt files for each step, similar to your
    second code snippet's approach.

    Returns a combined text result containing each step's final message.
    """

    # ----------------------------------------------
    # 1) Define which local prompt files to read per scenario
    #    (Adjust the file paths as you need!)
    # ----------------------------------------------
    prompts_map = {
        "spy": {
            "step1": "llm/spy_stalk_prompt/first_step_spy_stalk.txt",
            "step2": "llm/spy_stalk_prompt/second_step_spy_stalk.txt",
            "step3": "llm/spy_stalk_prompt/third_step_spy_stalk.txt"
        },
        "overload": {
            "step1": "llm/overloading_prompt/first_step_overloading.txt",
            "step2": "llm/overloading_prompt/second_step_overloading.txt"
        },
        "lockout": {
            "step1": "llm/lockout_prompt/first_step_lock.txt",
            "step2": "llm/lockout_prompt/second_step_lock.txt"
        },
        "impersonation": {
            "step1": "llm/impersonation_prompt/first_step_impersonation.txt",
            "step2": "llm/impersonation_prompt/second_step_impersonation.txt"
        }
    }

    if scenario not in prompts_map:
        raise ValueError(f"Scenario '{scenario}' is not defined in prompts_map.")

    # Prepare the LLM client
    client = Groq(api_key="")

    # We will store the entire conversation as a list of messages
    messages = []
    combined_result = []

    # ----------------------------------------------
    # 2) Round 1
    # ----------------------------------------------
    step1_file = prompts_map[scenario].get("step1")
    if not step1_file or not os.path.exists(step1_file):
        raise FileNotFoundError(f"Could not find prompt file: {step1_file}")

    # Read the step-1 prompt from local file
    with open(step1_file, 'r', encoding='utf-8') as file:
        step1_prompt = file.read()

    # Add the system + user messages for Round 1
    # System message is the text from the local prompt file
    messages.append({"role": "system", "content": step1_prompt})
    # Then, user message contains the actual shortcut text
    messages.append({"role": "user", "content": f"{shortcut_text}\n"})

    # Call the LLM
    completion1 = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=messages,
        temperature=0.8,
        max_completion_tokens=8192,
        top_p=0.9,
        stream=False
    )
    step1_answer = completion1.choices[0].message.content

    # Add the assistant response back to the conversation
    messages.append({"role": "assistant", "content": step1_answer})
    # Store for final results
    combined_result.append(f"--- Round 1 ({scenario}) ---\n{step1_answer}\n")

    # ----------------------------------------------
    # 3) Round 2
    # ----------------------------------------------
    step2_file = prompts_map[scenario].get("step2")
    if step2_file and os.path.exists(step2_file):
        with open(step2_file, 'r', encoding='utf-8') as file:
            step2_prompt = file.read()

        # Add the new system message from step2
        messages.append({"role": "system", "content": step2_prompt})

        # Call the LLM
        completion2 = client.chat.completions.create(
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            messages=messages,
            temperature=0.8,
            max_completion_tokens=2000,
            top_p=0.9,
            stream=False
        )
        step2_answer = completion2.choices[0].message.content
        messages.append({"role": "assistant", "content": step2_answer})
        combined_result.append(f"--- Round 2 ({scenario}) ---\n{step2_answer}\n")

    # ----------------------------------------------
    # 4) (Optional) Round 3 (if present)
    # ----------------------------------------------
    step3_file = prompts_map[scenario].get("step3")
    if step3_file and os.path.exists(step3_file):
        with open(step3_file, 'r', encoding='utf-8') as file:
            step3_prompt = file.read()

        messages.append({"role": "system", "content": step3_prompt})

        completion3 = client.chat.completions.create(
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            messages=messages,
            temperature=0.8,
            max_completion_tokens=2000,
            top_p=0.9,
            stream=False
        )
        step3_answer = completion3.choices[0].message.content
        messages.append({"role": "assistant", "content": step3_answer})
        combined_result.append(f"--- Round 3 ({scenario}) ---\n{step3_answer}\n")

    # If a scenario only has 2 steps defined, it will skip the 3rd step gracefully.

    # ----------------------------------------------
    # 5) Combine everything into one string
    # ----------------------------------------------
    final_output = "\n".join(combined_result)

    return final_output


def call_api_for_scenarios(txt_file_path):
    """
    Reads the text from `txt_file_path`,
    loops over 4 scenarios, calls the Groq LLM in multiple rounds,
    and writes out 4 separate results (one for each scenario).
    """
    # Step 1: Read the text from file
    with open(txt_file_path, 'r', encoding='utf-8') as f:
        shortcut_text = f.read()

    # Define your 4 scenarios
    scenarios = ["spy", "overload", "lockout", "impersonation"]

    # Loop over scenarios, each scenario has multiple LLM calls
    for scenario in scenarios:
        scenario_result = run_multiple_rounds(shortcut_text, scenario)
        # Write each scenario to a separate file
        base_name = os.path.splitext(txt_file_path)[0]  # remove '.txt' extension
        output_file = f"{base_name}_{scenario}.txt"
        with open(output_file, 'w', encoding='utf-8') as out_f:
            out_f.write(scenario_result)

        print(f"Scenario '{scenario}' completed. Result stored in: {output_file}")

def format_result(result):
    """Format the tuple (metadata, trigger, actions, output) into a string."""
    metadata, trigger, actions, output = result
    return actions



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
    all_false_count = -1
    total = -2
    if type == 'single':
        action_counts_df, all_false_count = calculate_result_of_folder.process_path(
                analysis_output_dir,
                f"{result_category_path}.txt")
        total = 1
    else:
        action_counts_df, all_false_count = calculate_result_of_folder.process_path(
                    analysis_output_dir,
                    result_category_path
        )
        total = len(link)

    # If every shortcut shows no True actions, we can skip the expensive LLM call

    # if all_false_count == total:
    #     print(f"No attacks detected in {total} shortcut(s). Skipping LLM analysis.")
    #     return

    # Otherwise, we need to escalate to an LLM for a deeper audit.

    # At this point, if all attack are shown as False, then we do not need to run the LLM.
    # If you need to run the LLM, there are two options:
    # 1. Run the LLM through API, in this case, we do not filter the token length as we do not know what kind of API you are using -- we will provide an example one.
    if type == 'single':
        with open(f"{yaml_output_dir}.txt", 'r', encoding='utf-8') as f:
            shortcut_text = f.read()
        scenarios = ["spy", "overload", "lockout", "impersonation"]
        for scenario in scenarios:
            scenario_result = run_multiple_rounds(shortcut_text, scenario)
            # Write each scenario to a separate file
            base_name = os.path.splitext(yaml_output_dir)[0]  # remove '.txt' extension
            output_file = f"{base_name}_{scenario}.txt"
            with open(output_file, 'w', encoding='utf-8') as out_f:
                out_f.write(scenario_result)

            print(f"Scenario '{scenario}' completed. Result stored in: {output_file}")
    else:
        os.makedirs(f"{yaml_output_dir}_results", exist_ok=True)
        # For batch processing, we can run the LLM on all files in the folder.
        for item in os.listdir(yaml_output_dir):
            file_path = os.path.join(yaml_output_dir, item)
            with open(file_path, 'r', encoding='utf-8') as f:
                shortcut_text = f.read()
            scenarios = ["spy", "overload", "lockout", "impersonation"]
            for scenario in scenarios:
                scenario_result = run_multiple_rounds(shortcut_text, scenario)
                # Write each scenario to a separate file
                base_name = os.path.splitext(item)[0]
                output_file = os.path.join(f"{yaml_output_dir}_results", f"{base_name}_{scenario}.txt")
                with open(output_file, 'w', encoding='utf-8') as out_f:
                    out_f.write(scenario_result)
                print(f"Scenario '{scenario}' for {item} completed. Result stored in: {output_file}")
        print("All scenarios processed for batch. Results stored in the 'results' subfolder.")


    # 2. Run a local LLM, in this case, we provide an example of filtering the token length, and using Qwen-32B-Instruct-Coder to analyze the results.
    # Please refer to the llm/run_llm.py file for more details.


if __name__ == "__main__":
    # main('https://www.icloud.com/shortcuts/0854ca93a7fd4d1bbd44a2f895e1b4b2', type='single')
    # Example usage for batch processing
    main(['https://www.icloud.com/shortcuts/34df135ad7be43799e8e8d10a6732fe8', 'https://www.icloud.com/shortcuts/0854ca93a7fd4d1bbd44a2f895e1b4b2'], type='batch')
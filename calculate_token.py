import argparse
import os
from tqdm import tqdm
from transformers import AutoTokenizer

'''
This script calculates the number of tokens in YAML files and categorizes them
based on a token limit. It can accept either:

1) A directory (containing the four specific .txt files), in which case it:
     - Looks for Impersonation.txt, Overload.txt, 
       SpywareStalkerware_Data_Exfiltration.txt, Lockout_Control.txt
     - For each .txt, reads its lines as YAML filenames under a YAML‐folder.
     - Splits those YAMLs into “safe” vs. “unsafe” and writes output files.

2) A single .txt file, in which case:
     - --yaml_path must be a single YAML file.
     - The script token‐counts that one YAML and simply prints “SAFE” or “UNSAFE”,
       without creating any output files.
'''

def calculate_token(tokenizer, file_path, overhead=1156):
    """
    Read the YAML file at `file_path`, encode it with `tokenizer`,
    and return len(token_ids) + overhead.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    token_ids = tokenizer.encode(text)
    return len(token_ids) + overhead

def process_single_txt_mode(txt_file_path, yaml_file_path, max_tokens, tokenizer):
    """
    SINGLE‐FILE MODE:
    - txt_file_path: path to one .txt (used only for naming/console output)
    - yaml_file_path: path to one YAML file to be token‐counted.
    Prints “SAFE” or “UNSAFE” based on token count; does not write any files.
    """
    base_txt = os.path.basename(txt_file_path)
    yaml_basename = os.path.basename(yaml_file_path)

    print(f"\n--- Single‐file mode: '{base_txt}' against YAML '{yaml_basename}' ---")
    if not os.path.isfile(yaml_file_path):
        print(f"Error: '{yaml_file_path}' is not a valid file.")
        return

    token_count = calculate_token(tokenizer, yaml_file_path)
    print(f"Token count for '{yaml_basename}': {token_count}  (threshold = {max_tokens})")

    if token_count < max_tokens:
        print(f"→ '{yaml_basename}' is SAFE")
    else:
        print(f"→ '{yaml_basename}' is UNSAFE")

def process_directory_mode(folder_path, yaml_folder_path, max_tokens, tokenizer):
    """
    DIRECTORY MODE:
    - folder_path: directory containing the four expected .txt files
    - yaml_folder_path: directory containing YAML files
    - For each of those .txt files, produce <TXT>_safe.txt and <TXT>_unsafe.txt lists.
    """
    target_txts = {
        "Impersonation.txt",
        "Overload.txt",
        "SpywareStalkerware_Data_Exfiltration.txt",
        "Lockout_Control.txt"
    }

    if not os.path.isdir(yaml_folder_path):
        print(f"Error: YAML folder '{yaml_folder_path}' does not exist.")
        return

    for entry in os.listdir(folder_path):
        if entry not in target_txts or not entry.endswith(".txt"):
            continue

        txt_file_path = os.path.join(folder_path, entry)
        if not os.path.isfile(txt_file_path):
            continue

        base_txt = os.path.basename(txt_file_path)
        print(f"\n--- Processing '{base_txt}' in directory mode ---")

        # Read all YAML filenames listed inside the .txt
        with open(txt_file_path, 'r', encoding='utf-8') as tf:
            yaml_filenames = [line.strip() for line in tf if line.strip()]

        list_under_safe = []
        under_safe_total = 0
        list_above_safe = []
        above_safe_total = 0

        for yaml_name in tqdm(yaml_filenames, desc=f"  Counting tokens for {base_txt}"):
            yaml_path = os.path.join(yaml_folder_path, yaml_name)
            if not os.path.isfile(yaml_path):
                # Skip missing YAMLs
                continue

            token_count = calculate_token(tokenizer, yaml_path)
            if token_count < max_tokens:
                list_under_safe.append((yaml_name, token_count))
                under_safe_total += token_count
            else:
                list_above_safe.append((yaml_name, token_count))
                above_safe_total += token_count

        # Write out the two list files next to the original .txt
        safe_out   = os.path.join(folder_path, f"{base_txt}_safe.txt")
        unsafe_out = os.path.join(folder_path, f"{base_txt}_unsafe.txt")

        with open(safe_out, 'w', encoding='utf-8') as sf:
            for name, _ in list_under_safe:
                sf.write(f"{name}\n")

        with open(unsafe_out, 'w', encoding='utf-8') as uf:
            for name, _ in list_above_safe:
                uf.write(f"{name}\n")

        # Print summary
        print(f"  {base_txt}: Total tokens under limit = {under_safe_total}")
        print(f"  {base_txt}: Total tokens above limit = {above_safe_total}")
        if list_under_safe:
            avg_under = under_safe_total / len(list_under_safe)
            print(f"    → Avg tokens (under): {avg_under:.2f}")
        else:
            print(f"    → No files under safe limit.")
        if list_above_safe:
            avg_above = above_safe_total / len(list_above_safe)
            print(f"    → Avg tokens (above): {avg_above:.2f}")
        else:
            print(f"    → No files above safe limit.")

        print(f"  → Safe list saved to   '{safe_out}'")
        print(f"  → Unsafe list saved to '{unsafe_out}'")

def main():
    parser = argparse.ArgumentParser(
        description="Calculate token counts for YAML files (single or directory mode)."
    )
    parser.add_argument(
        "input_path",
        type=str,
        help=(
            "Either:\n"
            "  1) A directory containing the four specific .txt files, OR\n"
            "  2) A single .txt file (to compare against exactly one YAML)."
        )
    )
    parser.add_argument(
        "yaml_path",
        type=str,
        help=(
            "If input_path is a DIRECTORY: yaml_path must be a YAML folder.\n"
            "If input_path is a SINGLE .txt: yaml_path must be a single YAML file."
        )
    )
    parser.add_argument(
        "--max_tokens",
        type=int,
        default=2057152,
        help="Token limit threshold (default: 2057152)."
    )
    args = parser.parse_args()

    input_path    = args.input_path
    yaml_path_arg = args.yaml_path
    max_tokens    = args.max_tokens

    tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-Coder-32B-Instruct")

    # Directory mode
    if os.path.isdir(input_path):
        if not os.path.isdir(yaml_path_arg):
            print(f"Error: When 'input_path' is a directory, 'yaml_path' must also be a directory.")
            return
        process_directory_mode(input_path, yaml_path_arg, max_tokens, tokenizer)

    # Single-file mode
    elif os.path.isfile(input_path) and input_path.lower().endswith(".txt"):
        if not os.path.isfile(yaml_path_arg):
            print(f"Error: When 'input_path' is a .txt file, 'yaml_path' must be a single YAML file.")
            return
        process_single_txt_mode(input_path, yaml_path_arg, max_tokens, tokenizer)

    else:
        print(f"Error: '{input_path}' is neither a valid directory nor a .txt file.")
        return

if __name__ == "__main__":
    main()

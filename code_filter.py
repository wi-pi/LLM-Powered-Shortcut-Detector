import argparse
import csv
import os
import sys
import traceback
import re
from tqdm import tqdm
import yaml

resource_control = ['Open App', 'Play Music', 'Show Alert', 'Add Alarm', 'Delete Alarm', 'Adjust Date', 'Dictate Text', 'Quick Look', 'Run Shortcut', 'Open X-Callback URL', 'Run Script over SSH', 'Stop and Output', 'Set Flashlight', 'Set Focus', 'Set Bluetooth', 'Set Wi-Fi', 'Set Airplane Mode', 'Shutdown', 'Set Low Power Mode', 'Set Appearance', 'Set AirDrop Receiving', 'Set VPN', 'Set Personal Hotspot', 'Set Cellular Data', 'Lock Screen', 'Set Night Shift', 'Set True Tone', 'Set Brightness', 'Set Orientation Lock', 'Go to Home Screen', 'Play Sound', 'Vibrate Device', 'Reset Cellular Data Statistics', 'Set Wallpaper Photo', 'Switch Between Wallpapers', 'Request Ride', 'Set Parked Car', 'Print', 'Move File', 'Rename File', 'Save File', 'Delete Files', 'Open File', 'Open URLs', 'Run JavaScript on Active Safari Tab', 'Remove from Photo Album', 'Delete Photos', 'Set Volume', 'Play/Pause', 'Skip Back', 'Skip Forward', 'Set Noise Control Mode', 'Handoff Playback', 'Change Playback Destination', 'Add to Playing Next', 'Clear Playing Next', 'Follow Podcast', 'Play Podcast', 'Remove Events', 'Set Calendar Focus Filter', 'Toggle Alarm', 'Lap Stopwatch', 'Reset Stopwatch', 'Start Stopwatch', 'Stop Stopwatch', 'Open Tab', 'Cancel Timer', 'Pause Timer', 'Resume Timer', 'Start Timer', 'Open Mailbox', 'Delete Notes', 'Show Quick Note', 'Open Notes View', 'Delete Folders', 'Move Notes to Folder', 'Delete Tags', 'Open Tag', 'Open Card', 'Set Data Roaming', 'Set LED Flash', 'Set Classic Invert', 'Set Color Filters', 'Set Increase Contrast', 'Set Smart Invert', 'Set Text Size', 'Auto-Answer Calls', 'Change Background Sounds', 'Open Magnifier', 'Set AssistiveTouch', 'Set Audio Descriptions', 'Set Background Sound Volume', 'Set Left/Right Audio Balance', 'Set Closed Captions+SDH', 'Call', 'Open Reminders List', 'Open Smart List', 'Remove Reminders', 'Play Recording', 'Change Recording Playback Setting', 'Stop Recording', 'Delete Recording', 'Create Alarm', 'Toggle Alarm', 'Close Safari Tab', 'Open Shortcut', 'Create Album', 'Delete Shortcut', 'Set Silent Mode', 'Set Zoom', 'Set Sound Detection', 'Set Voice Control', 'Set Live Captions', 'Set Mono Audio', 'Set Announce Notifications', 'Ping My Phone with lights on Watch', 'Set Flashlight on Watch', 'Set Theater Mode on Watch', 'Set Water Lock on Watch', 'Set School Time on Watch', 'Set VoiceOver', 'Run Home Scene', 'Set Hotspot Password', 'Open Camera Mode', 'Set Background Sounds', 'Set Voice Data Mode', 'Toggle Cellular Plan', 'Open Shortcut', 'Set Recognized Sounds', 'Add Shortcut to Home Screen', 'Delete Alarm', 'Set Silence Unknown Callers', 'Create New Private Tab in Safari', 'Set Default Cellular Plan', 'Create New Tab in Safari', 'Open Tab Group in Safari', 'Open Bookmark in Safari', 'Open View in Safari']
data_collection = ['Dictionary', 'Get Last Photos', 'Ask for Input', 'Get My Shortcuts', "Get What's On Screen", 'Take Photo', 'Take Video', 'Record Audio', 'Take Screenshot', 'Get Device Details', 'Get Battery Status', 'Get Orientation', 'Get Physical Activity', 'Get Clipboard', 'Get Current IP Address', 'Get Network Details', 'Get Hotspot Password', 'Get All Wallpapers', 'Get Current Location', 'Filter Locations', 'Get Parked Car Location', 'Get Text from PDF', 'Select File', 'Get Link to File', 'Get Contents of Folder', 'Get File from Folder', 'Filter Files', 'Filter Articles', 'Filter Images', 'Select Photos', 'Find Photos', 'Get Latest Videos', 'Get Latest Screenshots', 'Get Latest Bursts', 'Get Latest Live Photos', 'Get Last Import', 'Find Music', 'Get Current Song', 'Find Health Samples', 'Log Health Sample', 'Log Workout', 'Filter Event Attendees', 'Get Upcoming Events', 'Find Calendar Events', 'Find Alarms', 'Get State of Home', 'Select Email Address', 'Find Notes', 'Show Passwords', 'Find Developer Settings', 'Find Reminders', 'Get Upcoming Reminders', 'Create Recoding', 'Create Recording', 'Select Recording', 'Stop Recording', 'Select Contact', 'Select Phone Number', 'Find Contacts', 'Find Tabs', 'Open Camera Mode', 'Get Object of Class', 'Get Details of Workflow', 'Create iCloud Link', 'Filter Cellular Plan', 'Filter the Safari Reading List', 'Get Details of Note', 'Get Details of Shazam', 'Get Details of iTunes Artist', 'Filter Bookmark in Safari', 'Filter Tab Group in Safari']
data_insertion = ['Send Message', 'Text', 'Show Alert', 'List', 'Speak Text', 'Open X-Callback URL', 'Run Script over SSH', 'Send Email', 'Generate QR Code', 'Markup', 'Save File', 'Create Folder', 'Append to Text File', 'Open URLs', 'Get Contents of URL', 'Get Contents of Web Page', 'Run JavaScript on Active Safari Tab', 'Add Frame to GIF', 'Save to Photo Album', 'Add to Playlist', 'Create Playlist', 'Add New Calendar', 'Add New Event', 'Append to Note', 'Create Note', 'Pin Notes', 'Create Folder', 'Add Tags to Notes', 'Create Tag', 'Send Payment', 'Send WhatsApp Message', 'Send Photo via WhatsApp', 'Add New Reminder', 'Create Reminder List', 'Create Shortcut', 'Add New Contact']
data_exfiltration = ['Send Message', 'Choose from List', 'Show Result', 'Show Alert', 'Choose from Menu', 'Dictate Text', 'Speak Text', 'View Content Graph', 'Quick Look', 'Open X-Callback URL', 'Run Script over SSH', 'Stop and Output', 'Play Sound', 'Set Wallpaper Photo', 'Share', 'Share with Apps', 'Send Email', 'AirDrop', 'Post to Shared Album', 'Open URLs', 'Show Web View', 'Run JavaScript on Active Safari Tab', 'Open in Calendar', 'FaceTime', 'Open Note', 'Show Quick Note', 'Send Payment', 'Call', 'Send WhatsApp Message', 'Send Photo via WhatsApp', 'Show in iTunes Store', 'Open Shortcut', 'Transcribe Audio To Text']
trace_hiding = ['Base64 Encode', 'Generate Hash', 'Run Script over SSH', 'Generate QR Code', 'Run JavaScript on Active Safari Tab', 'Encode Media']
data_exfiltration_to_victim = ['Choose from List', 'Show Result', 'Show Alert', 'Choose from Menu', 'Dictate Text', 'Speak Text', 'View Content Graph', 'Quick Look', 'Stop and Output', 'Play Sound', 'Set Wallpaper Photo', 'Open in Calendar', 'Open Note', 'Show Quick Note', 'Show in iTunes Store', 'Open Shortcut', 'Transcribe Audio To Text']
data_exfiltration_to_other_without_user_action = ['Send Message', 'Open X-Callback URL', 'Run Script over SSH', 'Send Email', 'Post to Shared Album', 'Open URLs', 'Show Web View', 'Run JavaScript on Active Safari Tab', 'FaceTime', 'Send Payment', 'Call', 'Send WhatsApp Message', 'Send Photo via WhatsApp']


def code_analysis(input_path, output_path, debug=False):
    try:
        # Read the entire YAML content from the input file
        with open(input_path, 'r', encoding='utf-8') as file:
            data = yaml.safe_load(file)

        # Perform the analyses using the parsed data
        lockout_control = lockout_control_analysis(data, debug)
        spy_stalk = track_data_exfiltration(data, debug)
        impersonation = impersonation_check(data, debug)
        overload = overloading_check(data, debug)
        # toxic_content = toxic_content_check(data, debug)

        # Prepare the output
        output = []
        output.append(f"Lockout Control: {lockout_control}")
        output.append(f"Spyware/Stalkerware Data Exfiltration: {spy_stalk}")
        output.append(f"Impersonation: {impersonation}")
        output.append(f"Overload: {overload}")
        # output.append(f"Toxic Content: {toxic_content}")

        # Write the output to the output file
        with open(output_path, 'w', encoding='utf-8') as f:
            for line in output:
                f.write(line + '\n')

    except Exception as e:
        # Log errors with context and details
        error_log_path = "error_test.txt"
        with open(error_log_path, "a", encoding="utf-8") as error_log:
            error_message = f"Error processing file {input_path}:\n"
            error_details = f"{str(e)}\n{traceback.format_exc()}\n"
            print(error_details)
            error_log.write(error_message)
            error_log.write(error_details)

def action_distribution_analysis(data, action_map):
    if not isinstance(data, list):
        data = [data]

    for index, action_item in enumerate(data):
        try:
            if not action_item:
                continue  # Skip empty or invalid items

            first_key = next(iter(action_item.keys()))

            if first_key in action_map:
                action_map[first_key] += 1
            else:
                action_map[first_key] = 1
        except Exception as e:
            error_message = f"Error parsing action at index {index}: {action_item}\n{e}"
            raise Exception(error_message)
    return action_map

def lockout_control_analysis(data, debug=False):
    if not isinstance(data, list):
        data = [data]

    result = False

    for index, action_item in enumerate(data):
        try:
            if not action_item:
                continue  # Skip empty or invalid items

            first_key = next(iter(action_item.keys()))

            if first_key in ['Choose from List', 'Ask for Input', 'Choose from Menu']:
                return False

            if first_key in resource_control:
                if debug:
                    print(f"Lockout Control Detected at index {index}: Action '{first_key}'")
                result = True
        except Exception as e:
            error_message = f"Error parsing action at index {index}: {action_item}\n{e}"
            raise Exception(error_message)
    return result

def toxic_content_check(data, debug=False):
    data_insertion_exist = False

    if not isinstance(data, list):
        data = [data]

    for index, action_item in enumerate(data):
        try:
            if not action_item:
                continue

            first_key = next(iter(action_item.keys()))

            if first_key in data_insertion:
                if debug:
                    print(f"Data Insertion at index {index}: Action '{first_key}'")
                data_insertion_exist = True
            if data_insertion_exist:
                if first_key in data_exfiltration:
                    if debug:
                        print(f"Data Exfiltration at index {index}: Action '{first_key}'")
                    return True
        except Exception as e:
            error_message = f"Error parsing action at index {index}: {action_item}\n{e}"
            raise Exception(error_message)
    return False

def track_data_exfiltration(data, debug=False):
    # Map UUID to action and its data
    uuid_actions = {}
    # Map UUID to list of UUIDs it references
    uuid_references = {}
    # Set of UUIDs for data collection actions
    collection_uuids = set()
    # Map UUID to index for debugging
    uuid_indices = {}

    if not isinstance(data, list):
        data = [data]

    for index, action_item in enumerate(data):
        try:
            if not action_item:
                continue  # Skip empty or invalid items

            # Extract the first key and its corresponding content
            action, content = next(iter(action_item.items()))
            action_data = None
            uuid = None

            if isinstance(content, dict):
                action_data = content.get('data', {})
                uuid = content.get('uuid', None)
            else:
                continue  # Skip if content is not a dict

            if uuid:
                uuid_actions[uuid] = (action, action_data)
                uuid_indices[uuid] = (index, action)

            # Check if this is a data collection action
            if action in data_collection and uuid:
                collection_uuids.add(uuid)

            # Build UUID references
            referenced_uuids = []
            extract_uuids_from_value(action_data, referenced_uuids)

            if uuid:
                uuid_references[uuid] = referenced_uuids

        except Exception as e:
            error_message = f"Error parsing action at index {index}: {action_item}\n{e}"
            raise Exception(error_message)

    # Now, for each data exfiltration action, check if it (directly or indirectly) uses data from a data collection action
    def dfs(uuid, visited, path):
        if uuid in visited:
            return False
        visited.add(uuid)
        path.append(uuid)
        if uuid in collection_uuids:
            return True
        for ref_uuid in uuid_references.get(uuid, []):
            if dfs(ref_uuid, visited, path):
                return True
        path.pop()
        return False

    for uuid, (action, action_data) in uuid_actions.items():
        if action in data_exfiltration_to_other_without_user_action:
            visited = set()
            path = []
            if dfs(uuid, visited, path):
                if debug:
                    # Print the actions involved in the data exfiltration
                    print("Data Exfiltration Detected:")
                    for uid in reversed(path):
                        index, act = uuid_indices.get(uid, ("Unknown", "Unknown"))
                        print(f"Action '{act}' at index {index} with UUID {uid}")
                    # Include the exfiltration action itself
                    index, act = uuid_indices.get(uuid, ("Unknown", "Unknown"))
                    print(f"Action '{act}' at index {index} with UUID {uuid} (Exfiltration Action)")
                return True

    # If no exfiltration of collected data is detected
    return False

def extract_uuids_from_value(value, referenced_uuids):
    if isinstance(value, dict):
        if 'uuid' in value:
            referenced_uuid = value.get('uuid')
            if referenced_uuid:
                referenced_uuids.append(referenced_uuid)
        for sub_value in value.values():
            extract_uuids_from_value(sub_value, referenced_uuids)
    elif isinstance(value, list):
        for item in value:
            extract_uuids_from_value(item, referenced_uuids)
    # Strings and other types are ignored

def impersonation_check(data, debug=False):
    if not isinstance(data, list):
        data = [data]

    for index, action_item in enumerate(data):
        try:
            if not action_item:
                continue  # Skip empty or invalid items

            first_key = next(iter(action_item.keys()))

            if first_key in data_exfiltration_to_other_without_user_action:
                if debug:
                    print(f"Impersonation at index {index}: Action '{first_key}'")
                return True
        except Exception as e:
            error_message = f"Error parsing action at index {index}: {action_item}\n{e}"
            raise Exception(error_message)
    return False

def overloading_check(data, debug=False):
    repeat_stack = []

    if not isinstance(data, list):
        data = [data]

    for index, action_item in enumerate(data):
        try:
            if not action_item:
                continue

            first_key = next(iter(action_item.keys()))

            if first_key in ['Choose from List', 'Ask for Input', 'Choose from Menu']:
                return False

            if first_key in ['Repeat with Each', 'Repeat']:
                # Toggle repeat state: Start or End
                if repeat_stack and repeat_stack[-1] == first_key:
                    # End of a repeat block
                    repeat_stack.pop()
                    if debug:
                        print(f"Exiting repeat block at index {index}")
                else:
                    # Start of a new repeat block
                    repeat_stack.append(first_key)
                    if debug:
                        print(f"Entering repeat block at index {index}")
            elif repeat_stack:
                # If inside a repeat block, check for critical actions
                if first_key in resource_control or first_key in data_exfiltration:
                    if debug:
                        print(f"Overloading Detected at index {index}: Action '{first_key}' inside repeat block")
                    return True
        except Exception as e:
            error_message = f"Error parsing action at index {index}: {action_item}\n{e}"
            raise Exception(error_message)
    return False



def run_all(debug=False, input_folder_path=None, output_folder_path=None):
    if not input_folder_path or not output_folder_path:
        raise ValueError("Both input_folder_path and output_folder_path must be specified.")

    # Ensure output folder exists
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)

    # Open the error log file
    error_log_path = "error.txt"
    with open(error_log_path, "w", encoding="utf-8") as error_log:
        # Iterate through all `.txt` files in the input folder
        for filename in tqdm(os.listdir(input_folder_path)):
            if filename.endswith(".txt"):
                input_path = os.path.join(input_folder_path, filename)
                output_path = os.path.join(output_folder_path, filename)

                if debug:
                    print(f"Processing file: {input_path} -> {output_path}")
                try:
                    # Call the code_analysis function with the input and output paths
                    code_analysis(input_path, output_path, debug)
                except Exception as e:
                    # Capture the full traceback and write to the error log
                    error_message = f"Error processing {input_path}: {str(e)}\n"
                    traceback_details = traceback.format_exc()
                    print(error_message)
                    error_log.write(error_message)
                    error_log.write(traceback_details)
                    error_log.write("\n")

def resource_control_analysis(data, debug=False):
    if not isinstance(data, list):
        data = [data]

    result = False

    for index, action_item in enumerate(data):
        try:
            if not action_item:
                continue  # Skip empty or invalid items

            first_key = next(iter(action_item.keys()))

            if first_key in resource_control:
                if debug:
                    print(f"Lockout Control Detected at index {index}: Action '{first_key}'")
                result = True
        except Exception as e:
            error_message = f"Error parsing action at index {index}: {action_item}\n{e}"
            raise Exception(error_message)
    return result

def data_collection_analysis(data, debug=False):
    if not isinstance(data, list):
        data = [data]

    result = False

    for index, action_item in enumerate(data):
        try:
            if not action_item:
                continue  # Skip empty or invalid items

            first_key = next(iter(action_item.keys()))

            if first_key in data_collection:
                if debug:
                    print(f"Lockout Control Detected at index {index}: Action '{first_key}'")
                result = True
        except Exception as e:
            error_message = f"Error parsing action at index {index}: {action_item}\n{e}"
            raise Exception(error_message)
    return result

def data_insertion_analysis(data, debug=False):
    if not isinstance(data, list):
        data = [data]

    result = False

    for index, action_item in enumerate(data):
        try:
            if not action_item:
                continue  # Skip empty or invalid items

            first_key = next(iter(action_item.keys()))

            if first_key in data_insertion:
                if debug:
                    print(f"Lockout Control Detected at index {index}: Action '{first_key}'")
                result = True
        except Exception as e:
            error_message = f"Error parsing action at index {index}: {action_item}\n{e}"
            raise Exception(error_message)
    return result

def data_exfiltration_analysis(data, debug=False):
    if not isinstance(data, list):
        data = [data]

    result = False

    for index, action_item in enumerate(data):
        try:
            if not action_item:
                continue  # Skip empty or invalid items

            first_key = next(iter(action_item.keys()))

            if first_key in data_exfiltration:
                if debug:
                    print(f"Lockout Control Detected at index {index}: Action '{first_key}'")
                result = True
        except Exception as e:
            error_message = f"Error parsing action at index {index}: {action_item}\n{e}"
            raise Exception(error_message)
    return result

def trace_analysis(data, debug=False):
    if not isinstance(data, list):
        data = [data]

    result = False

    for index, action_item in enumerate(data):
        try:
            if not action_item:
                continue  # Skip empty or invalid items

            first_key = next(iter(action_item.keys()))

            if first_key in trace_hiding:
                if debug:
                    print(f"Lockout Control Detected at index {index}: Action '{first_key}'")
                result = True
        except Exception as e:
            error_message = f"Error parsing action at index {index}: {action_item}\n{e}"
            raise Exception(error_message)
    return result

def run_all_action_analyze_mapping(input_folder_path=None, output_file_path=None):

    action_map = {}

    # Initialize counters for the five operations
    data_collection_count = 0
    data_insertion_count = 0
    data_exfiltration_count = 0
    resource_control_count = 0
    trace_analysis_count = 0

    # Open the error log file
    error_log_path = "error_actions.txt"
    with open(error_log_path, "w", encoding="utf-8") as error_log:
        # Iterate through all `.txt` files in the input folder
        for filename in tqdm(os.listdir(input_folder_path)):
            if filename.endswith(".txt"):
                try:
                    input_path = os.path.join(input_folder_path, filename)
                    with open(input_path, 'r', encoding='utf-8') as file:
                        data = yaml.safe_load(file)

                    # Perform analysis for each type of operation
                    if data_collection_analysis(data):
                        data_collection_count += 1
                    if data_insertion_analysis(data):
                        data_insertion_count += 1
                    if data_exfiltration_analysis(data):
                        data_exfiltration_count += 1
                    if resource_control_analysis(data):
                        resource_control_count += 1
                    if trace_analysis(data):
                        trace_analysis_count += 1

                    # Update the action map
                    action_map = action_distribution_analysis(data, action_map)

                except Exception as e:
                    # Capture the full traceback and write to the error log
                    error_message = f"Error processing {input_path}: {str(e)}\n"
                    traceback_details = traceback.format_exc()
                    print(error_message)
                    error_log.write(error_message)
                    error_log.write(traceback_details)
                    error_log.write("\n")

    # Print summary of the counts
    print(f"Data collection: {data_collection_count}")
    print(f"Data insertion: {data_insertion_count}")
    print(f"Data exfiltration: {data_exfiltration_count}")
    print(f"Resource control: {resource_control_count}")
    print(f"Trace analysis: {trace_analysis_count}")


def run_all_action_analyze(input_folder_path=None, output_file_path=None):
    if not input_folder_path or not output_file_path:
        raise ValueError("Both input_folder_path and output_file_path must be specified.")

    action_map = {}
    # Open the error log file
    error_log_path = "error_actions.txt"
    with open(error_log_path, "w", encoding="utf-8") as error_log:
        # Iterate through all `.txt` files in the input folder
        for filename in tqdm(os.listdir(input_folder_path)):
            if filename.endswith(".txt"):
                try:
                    input_path = os.path.join(input_folder_path, filename)
                    with open(input_path, 'r', encoding='utf-8') as file:
                        data = yaml.safe_load(file)
                    action_map = action_distribution_analysis(data, action_map)
                except Exception as e:
                    # Capture the full traceback and write to the error log
                    error_message = f"Error processing {input_path}: {str(e)}\n"
                    traceback_details = traceback.format_exc()
                    print(error_message)
                    error_log.write(error_message)
                    error_log.write(traceback_details)
                    error_log.write("\n")

    # Write the action map to a CSV file
    with open(output_file_path, 'w', encoding='utf-8', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        # Write header
        csv_writer.writerow(['key', 'value'])
        # Write action map data
        for key, value in action_map.items():
            csv_writer.writerow([key, value])

import os
import yaml
import csv
import traceback
from tqdm import tqdm

def run_all_action_analyze_all(input_folder_paths, output_file_path):
    if not input_folder_paths or not output_file_path:
        raise ValueError("Both input_folder_paths and output_file_path must be specified.")

    if not isinstance(input_folder_paths, list) or len(input_folder_paths) == 0:
        raise ValueError("input_folder_paths must be a non-empty list of folder paths.")

    action_map = {}
    # Open the error log file
    error_log_path = "error_actions.txt"
    with open(error_log_path, "w", encoding="utf-8") as error_log:
        # Iterate through all input folders
        for input_folder_path in input_folder_paths:
            if not os.path.isdir(input_folder_path):
                error_message = f"Invalid directory: {input_folder_path}\n"
                print(error_message)
                error_log.write(error_message)
                continue

            # Process each `.txt` file in the current input folder
            for filename in tqdm(os.listdir(input_folder_path), desc=f"Processing folder: {input_folder_path}"):
                if filename.endswith(".txt"):
                    try:
                        input_path = os.path.join(input_folder_path, filename)
                        with open(input_path, 'r', encoding='utf-8') as file:
                            data = yaml.safe_load(file)
                        action_map = action_distribution_analysis(data, action_map)
                    except Exception as e:
                        # Capture the full traceback and write to the error log
                        error_message = f"Error processing {input_path}: {str(e)}\n"
                        traceback_details = traceback.format_exc()
                        print(error_message)
                        error_log.write(error_message)
                        error_log.write(traceback_details)
                        error_log.write("\n")

    # Write the combined action map to a CSV file
    with open(output_file_path, 'w', encoding='utf-8', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        # Write header
        csv_writer.writerow(['key', 'value'])
        # Write action map data
        for key, value in action_map.items():
            csv_writer.writerow([key, value])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Analyze YAML-based automation workflows.")
    parser.add_argument('--input', '-i', required=True, help='Path to the input YAML file or folder.')
    parser.add_argument('--output', '-o', required=True, help='Path to the output file or folder.')
    parser.add_argument('--debug', '-d', action='store_true', help='Enable debug mode for verbose output.')
    parser.add_argument('--mode', '-m', choices=['single', 'batch'], default='single',
                        help='Processing mode: single file or batch processing.')
    args = parser.parse_args()

    if args.mode == 'single':
        code_analysis(args.input, args.output, debug=args.debug)
    else:
        run_all(debug=args.debug, input_folder_path=args.input, output_folder_path=args.output)

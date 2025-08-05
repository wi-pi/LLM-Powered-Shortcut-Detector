import ast
import re

# Define separate functions for each action

def parse_get_attachment(input):
    if input is None or input == '':
        return ''

    res_list = []

    # Define a helper function to parse individual items
    def parse_item(item):
        if isinstance(item, dict):
            input_data = item.get('data', '')  # Default to empty string if 'data' is not found
            input_uuid = item.get('uuid', '')  # Default to empty string if 'uuid' is not found
            return f"{input_data} (uuid: {input_uuid})"
        elif isinstance(item, list):
            # Recursively parse list items
            return ', '.join(parse_item(sub_item) for sub_item in item)
        elif isinstance(item, str):
            return item.strip()
        else:
            # Handle other types if necessary
            return str(item)

    # Check if input is a list
    if isinstance(input, list):
        for item in input:
            parsed = parse_item(item)
            res_list.append(parsed)
    elif isinstance(input, dict) or isinstance(input, str):
        # If input is a single item, parse it directly
        parsed = parse_item(input)
        res_list.append(parsed)
    else:
        # Handle other types if necessary
        res_list.append(str(input))

    return ', '.join(res_list)

def parse_appendvariable(action_data):
    if action_data == '':
        return 'Add _ to _', 'None'
    variable_name = action_data.get('Variable Name')
    if variable_name is None or variable_name == '':
        variable_name = '_'

    input_data = action_data.get('Input')
    if input_data is not None:
        input_data = parse_get_attachment(input_data)
    else:
        input_data = '_'

    custom_name = action_data.get('Output Name')
    if custom_name is not None:
        return f"Add {input_data} to {variable_name} (output name: {custom_name})"
    else:
        return f"Add {input_data} to {variable_name}"


def parse_nested_dictionary(data, indent=0):
    if data is None:
        return ''

    res_list = []
    indent_str = '  ' * indent  # Indentation for nested levels

    if isinstance(data, list):
        for item in data:
            parsed_item = parse_nested_dictionary(item, indent)
            res_list.append(parsed_item)
    elif isinstance(data, dict):
        # Check if 'key' and 'value' are present
        key = data.get('key')
        value = data.get('value')
        if isinstance(key, list) and len(key) == 1:
            key = key[0]
        if isinstance(value, list) and len(value) == 1:
            value = value[0]

        # Recursively parse the value
        if isinstance(value, dict) or isinstance(value, list):
            value_str = parse_nested_dictionary(value, indent + 1)
        else:
            value_str = str(value)

        res_list.append(f"{indent_str}{key}: {value_str}")
    else:
        res_list.append(f"{indent_str}{data}")

    return '\n'.join(res_list)

def parse_dictionary(action_data):
    if action_data == '':
        return 'Dictionary: _'

    input_data = action_data.get('Input')
    if input_data is not None:
        parsed_dict = parse_nested_dictionary(input_data)
    else:
        parsed_dict = '_'

    custom_name = action_data.get('Custom Output Name')

    if custom_name:
        return f"Dictionary (output name: {custom_name}):\n{parsed_dict}"
    else:
        return f"Dictionary:\n{parsed_dict}"

def parse_gettext(action_data):
    if action_data == '':
        return 'Text: _'
    input_data = action_data.get('data', '_')
    if input_data == '':
        input_data = '_'
    return f"Text: {input_data}"

def parse_choosefromlist(action_data):
    if action_data == '':
        return 'Choose from _\n - Prompt: _ \n - Select Multiple: false'
    metadata = action_data.get('metadata', {})
    data = action_data.get('Input', [])
    res_data = parse_get_attachment(data)
    prompt = metadata.get('Prompt', '_')
    if prompt == '':
        prompt = '_'
    else:
        prompt = parse_get_attachment(prompt)
    select_multiple = metadata.get('Select Multiple', False)
    ans = f"Choose from {res_data}\n - Prompt: {prompt}\n - Select Multiple: {select_multiple}\n"
    if select_multiple:
        select_all = metadata.get('Select All Initially', False)
        ans += f" - Select All Initially: {select_all}\n"
    return ans


def parse_list(action_data):
    list_items = action_data.get('List Items', [])
    res = []
    if len(list_items) == 0:
        return 'List: [_]'

    def parse_item(item):
        if isinstance(item, str):
            if item == '':
                return '_'
            return item.strip()
        elif isinstance(item, dict):
            # Handle dictionaries with 'data' and 'uuid'
            data = item.get('data', '_')
            if data == '':
                data = '_'
            uuid = item.get('uuid', '')
            return f"{data} (uuid: {uuid})"
        elif isinstance(item, list):
            # Recursively parse list
            return ', '.join(parse_item(sub_item) for sub_item in item)
        else:
            # Handle other types
            return str(item)

    for item in list_items:
        parsed_item = parse_item(item)
        res.append(parsed_item)

    return f"List: [{', '.join(res)}]"

# Map action keys to their respective functions
action_map = {
    'is.workflow.actions.appendvariable': parse_appendvariable,
    'is.workflow.actions.dictionary': parse_dictionary,
    'is.workflow.actions.gettext': parse_gettext,
    'is.workflow.actions.choosefromlist': parse_choosefromlist,
    'is.workflow.actions.list': parse_list,
    # Add more action mappings here if needed
}

def process_actions(actions):
    human_readable_actions = []

    # actions is already a list of action strings
    dict_strings = actions

    for action_str in dict_strings:
        # print(f"Processing action string: {action_str}")  # Debug: print the raw action string

        # Parse the string as a Python dictionary using ast.literal_eval
        action_data = ast.literal_eval(action_str)
        # print(f"Parsed action data: {action_data}")  # Debug: print the parsed action data

        for key, value in action_data.items():
            # print(f"Processing action key: {key}, value: {value}")  # Debug: print the key-value pair

            # Find the corresponding function for the action key
            action_function = action_map.get(key)
            if action_function:
                # print(f"Calling function for action: {key}")  # Debug: indicate function is being called
                # Extract 'data' from value if it exists
                action_value_data = value.get('data')
                result = action_function(action_value_data)
                res_uuid = value.get('uuid')
                print(f"action: {result}, tracking uuid: {res_uuid}")  # Debug: print the result of the function
                human_readable_actions.append(f"Action: {result}, tracking uuid: {res_uuid}")
            else:
                print(f"Unknown action key: {key}")
                human_readable_actions.append(f"Unknown action: {key}")

    return "\n".join(human_readable_actions)



def parse_txt_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        raw_data = file.read()

    # Split the raw data into different sections using regular expressions
    sections = re.split(r'^(Metadata|Trigger|Actions|Output):\s*$', raw_data, flags=re.MULTILINE)

    data = {}
    current_section = None

    # Iterate over the sections
    i = 0
    while i < len(sections):
        section = sections[i].strip()
        if section in ["Metadata", "Trigger", "Actions", "Output"]:
            current_section = section
            content = sections[i + 1].strip() if i + 1 < len(sections) else ''
            # Split the content into lines and store as a list
            data[current_section] = content.split('\n')
            i += 2
        else:
            i += 1

    return data


def process_metadata(metadata):
    # Placeholder for processing metadata
    return f"Metadata: {metadata}"

def process_trigger(trigger):
    # Placeholder for processing trigger
    return f"Trigger: {trigger}"

def process_output(output):
    # Placeholder for processing output
    return f"Output: {output}"


def interpret_workflow(file_path):
    parsed_data = parse_txt_file(file_path)

    # Interpret each section
    metadata_output = process_metadata(parsed_data.get('Metadata', []))
    trigger_output = process_trigger(parsed_data.get('Trigger', []))
    actions_output = process_actions(parsed_data.get('Actions', []))
    output_output = process_output(parsed_data.get('Output', []))

    # Combine all interpretations
    final_output = "\n".join([metadata_output, trigger_output, actions_output, output_output])

    return final_output

# Example usage
# file_path = '../test.plist/test_result/test.plist-choosefromlist-list-addvariable.txt'  # Replace with your file path

# interpreted_workflow = interpret_workflow(file_path)
# print(interpreted_workflow)

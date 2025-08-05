import parse_xml.parse_shortcut_WF as helper


def action_choosefromlist(elem):
    """
    Extracts the 'Choose from List' action from the action.

    Parameters:
    - elem (Element): The XML element containing the 'Choose from List' action.

    Returns:
    - The 'Choose from List' action list.
    """
    if not helper.check_validation(elem):
        return helper.append_data({'Choose from': '', 'Prompt': '', 'Select Multiple': False}, None)
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.track_custom_name(elem)

    # Next: make a new function to record meta data {metadata:. data:, uuid:}
    select_multiple = helper.get_elements_after_key(elem, 'WFChooseFromListActionSelectMultiple', 'true')
    if select_multiple is not None:
        select_multiple = True
    else:
        select_multiple = False

    # Check on data
    # 1. Check if there are custom action prompt.txt
    custom_prompt = helper.extract_value_from_string_or_dict(elem, 'WFChooseFromListActionPrompt')
    if custom_prompt is None:
        custom_prompt = ''
    # 2. process the data
    data = helper.extract_value_from_string_or_dict(elem, 'WFInput')

    res = {'Choose from': data, 'Prompt': custom_prompt, 'Select Multiple': select_multiple}
    if custom_output_name is not None:
        res['Output Name'] = custom_output_name
    return helper.append_data(res, uuid)

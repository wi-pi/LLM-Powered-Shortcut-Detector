import parse_xml.parse_shortcut_WF as helper



def action_detectlanguage(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Input': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.track_custom_name(elem)

    # Get the input of the action -- must be a dict
    input_text = helper.extract_value_from_string_or_dict(elem, 'WFInput')
    if input_text is None:
        input_text = ''
    else:
        if len(input_text) == 0:
            input_text = ''

    res = {'Input': input_text}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
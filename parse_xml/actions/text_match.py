import parse_xml.parse_shortcut_WF as helper


def action_text_match(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Input': '', 'Pattern': '[0-9a-zA-Z]', 'Case Sensitive': True}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.get_elements_after_key(elem, 'CustomOutputName', 'string')
    if custom_output_name is not None:
        custom_output_name = custom_output_name[0].text

    # Get the input -- string or dict after text
    input_text_elem = helper.extract_value_from_string_or_dict(elem, 'text')
    if input_text_elem is None:
        input_text_elem = ''
    else:
        if len(input_text_elem) == 0:
            input_text_elem = ''

    res = {'Input': input_text_elem}

    # Get the pattern
    pattern = helper.extract_value_from_string_or_dict(elem, 'WFMatchTextPattern')
    if pattern is None:
        pattern = '[0-9a-zA-Z]'

    res['Pattern'] = pattern


    # Get the case sensitive
    case_sensitive = helper.get_elements_after_key(elem, 'WFMatchTextCaseSensitive', 'false')
    if case_sensitive is None:
        case_sensitive = True
    else:
        case_sensitive = False
    res['Case Sensitive'] = case_sensitive


    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
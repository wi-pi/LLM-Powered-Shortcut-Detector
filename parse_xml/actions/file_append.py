import parse_xml.parse_shortcut_WF as helper
import parse_xml_output.parse_output_to_natural_language as output_helper

def action_file_append(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Append': '', 'to': 'Shortcuts', 'File Path': '', 'Make New Line': True}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output name if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the append action
    append_action = helper.extract_value_from_string_or_dict(elem, 'WFAppendFileWriteMode')
    if append_action is None:
        append_action = 'Append'
    else:
        if type(append_action) == list:
            append_action = output_helper.parse_get_attachment(append_action)

    # Get the append input
    append_input = helper.extract_value_from_string_or_dict(elem, 'WFInput')
    if append_input is None:
        append_input = ''

    # Get the to input
    from_input = ''
    parse_elem = helper.get_elements_after_key(elem, 'WFFile', 'dict')
    if parse_elem is None:
        parse_elem = helper.get_elements_after_key(elem, 'WFFile', 'array')
    if parse_elem is not None:
        from_input = helper.parse_file_input(parse_elem[0], 'WFFile')
    if from_input is None:
        from_input = ''

    # Get the file path
    file_path = helper.extract_value_from_string_or_dict(elem, 'WFFilePath')
    if file_path is None:
        file_path = ''

    # Get the make new line
    make_new_line = helper.get_elements_after_key(elem, 'WFAppendOnNewLine', 'false')
    if make_new_line is not None:
        make_new_line = False
    else:
        make_new_line = True

    res = {append_action: append_input, 'to': from_input, 'File Path': file_path, 'Make New Line': make_new_line}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
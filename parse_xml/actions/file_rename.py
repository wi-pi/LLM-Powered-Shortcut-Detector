import parse_xml.parse_shortcut_WF as helper


def action_file_rename(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Rename': '', 'to': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output name if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the from input
    from_input = ''
    parse_elem = helper.get_elements_after_key(elem, 'WFFile', 'dict')
    if parse_elem is None:
        parse_elem = helper.get_elements_after_key(elem, 'WFFile', 'array')
    if parse_elem is not None:
        from_input = helper.parse_file_input(parse_elem[0], 'WFFile')
    if from_input is None:
        from_input = ''

    # Get the to input
    to_input = helper.extract_value_from_string_or_dict(elem, 'WFNewFilename')
    if to_input is None:
        to_input = ''

    res = {'Rename': from_input, 'to': to_input}
    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
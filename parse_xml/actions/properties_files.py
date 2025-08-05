import parse_xml.parse_shortcut_WF as helper


def action_properties_files(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Get': '', 'from': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output name if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the get type input
    get_type = helper.extract_value_from_string_or_dict(elem, 'WFContentItemPropertyName')
    if get_type is None:
        get_type = ''

    # Get the from input
    from_input = ''
    parse_elem = helper.get_elements_after_key(elem, 'WFInput', 'dict')
    if parse_elem is not None:
        from_input = helper.parse_file_input(parse_elem[0], 'WFInput')

    res = {'Get': get_type, 'from': from_input}
    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
import parse_xml.parse_shortcut_WF as helper


def action_file(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'File': ''}, None)

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

    res = {'File': from_input}
    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
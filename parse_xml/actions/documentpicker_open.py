import parse_xml.parse_shortcut_WF as helper


def action_documentpicker_open(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Get file from': 'Shortcuts', 'at path': '', 'Error If Not Found': True}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output name if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the from input
    from_input = 'Shortcuts'
    from_elem = helper.get_elements_after_key(elem, 'WFFile', 'dict')
    if from_elem is None:
        from_elem = helper.get_elements_after_key(elem, 'WFFile', 'array')
    if from_elem is not None:
        from_input = helper.parse_file_input(from_elem[0], 'WFFile')

    # Get file path
    file_path = helper.extract_value_from_string_or_dict(elem, 'WFGetFilePath')
    if file_path is None:
        file_path = ''

    # Get the error if not found
    error_if_not_found = helper.get_elements_after_key(elem, 'WFFileErrorIfNotFound', 'false')
    if error_if_not_found is not None:
        error_if_not_found = False
    else:
        error_if_not_found = True

    res = {'Get file from': from_input, 'at path': file_path, 'Error If Not Found': error_if_not_found}
    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
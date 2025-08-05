import parse_xml.parse_shortcut_WF as helper


def action_file_createfolder(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Create Folder in': 'Shortcuts', 'at': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output name if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the folder name
    folder_name = helper.get_elements_after_key(elem, 'WFFolder', 'dict')
    if folder_name is None:
        folder_name = 'Shortcuts'
    else:
        folder_name = helper.parse_file_input(folder_name[0], 'WFFolder')

    # Get the at input
    at_input = helper.extract_value_from_string_or_dict(elem, 'WFFilePath')
    if at_input is None:
        at_input = ''

    res = {'Create Folder in': folder_name, 'at': at_input}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
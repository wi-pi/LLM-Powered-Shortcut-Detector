import parse_xml.parse_shortcut_WF as helper


def action_file_getfoldercontents(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Get contents of folder': '', 'Recursive': False}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output name if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the folder name
    folder_name = helper.get_elements_after_key(elem, 'WFFolder', 'dict')
    if folder_name is None:
        folder_name = ''
    else:
        folder_name = helper.parse_file_input(folder_name[0], 'WFFolder')

   # Get the recursive
    recursive = helper.get_elements_after_key(elem, 'Recursive', 'true')
    if recursive is not None:
        recursive = True
    else:
        recursive = False

    res = {'Get contents of folder': folder_name, 'Recursive': recursive}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
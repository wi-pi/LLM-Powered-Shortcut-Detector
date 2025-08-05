import parse_xml.parse_shortcut_WF as helper


def action_show_notefolder(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Show Folder': 'Notes'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the folder
    folder = 'Notes'
    folder_elem = helper.get_elements_after_key(elem, 'folder', 'dict')
    if folder_elem is not None:
        folder = helper.extract_value_from_string_or_dict(folder_elem[0], 'displayString')
        if folder is None:
            folder = helper.extract_value_from_string_or_dict(elem, 'folder')
    if folder is None:
        folder = 'Notes'

    res = {'Show Folder': folder}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name
    return helper.append_data(res, uuid)
import parse_xml.parse_shortcut_WF as helper


def action_createnote(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Create note with': '', 'in': '', 'Name': '', 'Open When Run': True}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the content
    content = helper.extract_value_from_string_or_dict(elem, 'WFCreateNoteInput')
    if content is None:
        content = ''

    # Get the folder
    folder = ''
    folder_elem = helper.get_elements_after_key(elem, 'folder', 'dict')
    if folder_elem is not None:
        folder = helper.get_elements_after_key(folder_elem[0], 'title', 'dict')
        if folder is not None:
            folder = helper.extract_value_from_string_or_dict(folder[0], 'key')
        else:
            folder = helper.extract_value_from_string_or_dict(elem, 'folder')
    if folder is None:
        folder = ''

    # Get the name
    name = helper.extract_value_from_string_or_dict(elem, 'name')
    if name is None:
        name = ''

    # Get the Open When Run
    open_when_run = helper.get_elements_after_key(elem, 'OpenWhenRun', 'false')
    if open_when_run is None:
        open_when_run = True
    else:
        open_when_run = False

    res = {'Create note with': content, 'in': folder, 'Name': name, 'Open When Run': open_when_run}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name
    return helper.append_data(res, uuid)
import parse_xml.parse_shortcut_WF as helper


def action_delete_note_folder(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Delete the folder(s)': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)


    ## Get the note(s) to delete
    note = ''
    note_elem = helper.get_elements_after_key(elem, 'entities', 'array')
    if note_elem is None:
        note_elem = helper.get_elements_after_key(elem, 'entities', 'dict')
        if note_elem is not None:
            note = helper.parse_note(note_elem[0])
        else:
            note = helper.extract_value_from_string_or_dict(elem, 'entities')
            if note is None: note = ''
    else:
        if len(note_elem[0]) > 0:
            note = helper.parse_note(note_elem[0], 'array')

    res = {'Delete the folder(s)': note}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name
    return helper.append_data(res, uuid)
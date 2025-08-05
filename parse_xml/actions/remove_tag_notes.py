import parse_xml.parse_shortcut_WF as helper


def action_remove_tag_notes(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Remove the tag(s)': '', 'from': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the tag(s)
    tag = ''
    tag_elem = helper.get_elements_after_key(elem, 'tags', 'array')
    if tag_elem is None:
        tag_elem = helper.get_elements_after_key(elem, 'tags', 'dict')
        if tag_elem is not None:
            tag = helper.parse_note(tag_elem[0])
        else:
            tag = helper.extract_value_from_string_or_dict(elem, 'tags')
            if tag is None: tag = ''
    else:
        if len(tag_elem[0]) > 0:
            tag = helper.parse_note(tag_elem[0], 'array')

    # Get the note(s)
    note = ''
    note_elem = helper.get_elements_after_key(elem, 'notes', 'array')
    if note_elem is None:
        note_elem = helper.get_elements_after_key(elem, 'notes', 'dict')
        if note_elem is not None:
            note = helper.parse_note(note_elem[0])
        else:
            note = helper.extract_value_from_string_or_dict(elem, 'entities')
            if note is None: note = ''
    else:
        if len(note_elem[0]) > 0:
            note = helper.parse_note(note_elem[0], 'array')

    res = {'Remove the tag(s)': tag, 'from': note}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name
    return helper.append_data(res, uuid)
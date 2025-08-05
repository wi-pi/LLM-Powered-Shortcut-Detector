import parse_xml.parse_shortcut_WF as helper


def action_appendnote(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Append': '', 'to': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # Get content to append
    append = helper.extract_value_from_string_or_dict(elem, 'WFInput')
    if append is None:
        append = ''

    # Get the note
    note = ''
    note_elem = helper.get_elements_after_key(elem, 'WFNote', 'dict')
    if note_elem is not None:
        note = helper.parse_note(note_elem[0])

    res = {'Append': append, 'to': note}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name
    return helper.append_data(res, uuid)
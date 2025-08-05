import parse_xml.parse_shortcut_WF as helper


def action_shownote(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Open the Note': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the note
    note = ''
    note_elem = helper.get_elements_after_key(elem, 'WFInput', 'dict')
    if note_elem is not None:
        note = helper.parse_note(note_elem[0])

    res = {'Open the Note': note}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name
    return helper.append_data(res, uuid)
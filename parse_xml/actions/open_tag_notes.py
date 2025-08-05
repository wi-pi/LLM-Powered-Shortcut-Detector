import parse_xml.parse_shortcut_WF as helper


def action_open_tag_notes(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Open the tag': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the tag(s)
    tag = helper.get_elements_after_key(elem, 'target', 'dict')
    if tag is not None:
        tag = helper.parse_note(tag[0])
    else:
        tag = ''

    res = {'Open the tag': tag}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name
    return helper.append_data(res, uuid)
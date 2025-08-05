import parse_xml.parse_shortcut_WF as helper


def action_delete_tag_notes(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Delete the tag(s)': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the tag(s)
    tag = ''
    tag_elem = helper.get_elements_after_key(elem, 'entities', 'array')
    if tag_elem is None:
        tag_elem = helper.get_elements_after_key(elem, 'entities', 'dict')
        if tag_elem is not None:
            tag = helper.parse_note(tag_elem[0])
        else:
            tag = helper.extract_value_from_string_or_dict(elem, 'entities')
            if tag is None: tag = ''
    else:
        if len(tag_elem[0]) > 0:
            tag = helper.parse_note(tag_elem[0], 'array')

    res = {'Delete the tag(s)': tag}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name
    return helper.append_data(res, uuid)
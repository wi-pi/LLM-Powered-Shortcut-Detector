import parse_xml.parse_shortcut_WF as helper


def action_select_recording(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Open': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # Get recording
    item = helper.get_elements_after_key(elem, 'target', 'dict')
    play_item = ''
    if item is not None:
        play_item = helper.get_elements_after_key(item, 'title', 'dict')
        if play_item is None:
            play_item = helper.extract_value_from_string_or_dict(elem, 'target')
        else:
            play_item = helper.extract_value_from_string_or_dict(play_item[0], 'key')
    if play_item is not None:
        play_item = helper.list_to_str(play_item)

    res = {'Select': play_item}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name
    return helper.append_data(res, uuid)
import parse_xml.parse_shortcut_WF as helper


def action_play_recording(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Play': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # Get what to play
    play = helper.extract_value_from_string_or_dict(elem, 'playbackType')
    if play is None:
        play = 'Most Recent Recording'

    res = {'Play': play}

    if play == 'specific':
        item = helper.get_elements_after_key(elem, 'entity', 'dict')
        play_item = ''
        if item is not None:
            play_item = helper.get_elements_after_key(item, 'title', 'dict')
            if play_item is None:
                play_item = helper.extract_value_from_string_or_dict(elem, 'entity')
            else:
                play_item = helper.extract_value_from_string_or_dict(play_item[0], 'key')
        if play_item is not None:
            play_item = helper.list_to_str(play_item)

        res['Item'] = play_item

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name
    return helper.append_data(res, uuid)
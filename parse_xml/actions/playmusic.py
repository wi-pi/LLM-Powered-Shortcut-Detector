import parse_xml.parse_shortcut_WF as helper


def action_playmusic(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Play': '', 'Shuffle': 'Off', 'Repeat': 'None'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the music
    music = helper.extract_value_from_string_or_dict(elem, 'WFMediaItems')
    if music is None:
        music = ''

    # Get two opinions -- shuffle and repeat
    shuffle = helper.extract_value_from_string_or_dict(elem, 'WFPlayMusicActionShuffle')
    if shuffle is None:
        shuffle = 'Off'

    repeat = helper.extract_value_from_string_or_dict(elem, 'WFPlayMusicActionRepeat')
    if repeat is None:
        repeat = 'None'

    res = {'Play': music, 'Shuffle': shuffle, 'Repeat': repeat}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name
    return helper.append_data(res, uuid)

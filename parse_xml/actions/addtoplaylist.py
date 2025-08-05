import parse_xml.parse_shortcut_WF as helper


def action_addtoplaylist(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Add': '', 'to': 'My Music Library'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the music
    music = helper.extract_value_from_string_or_dict(elem, 'WFInput')
    if music is None:
        music = 'My Music Library'

    # Get the playlist
    playlist = helper.extract_value_from_string_or_dict(elem, 'WFPlaylistName')
    if playlist is None:
        playlist = ''

    res = {'Add': music, 'to': playlist}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
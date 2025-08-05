import parse_xml.parse_shortcut_WF as helper


def action_get_playlist(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Get songs in': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the playlist
    playlist = helper.extract_value_from_string_or_dict(elem, 'WFPlaylistName')
    if playlist is None:
        playlist = ''

    res = {'Get songs in': playlist}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
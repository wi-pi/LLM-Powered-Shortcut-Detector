import parse_xml.parse_shortcut_WF as helper


def action_createplaylist(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Create playlist': '', 'with': '', 'Author': '', 'Comment': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the playlist
    playlist = helper.extract_value_from_string_or_dict(elem, 'WFPlaylistName')
    if playlist is None:
        playlist = ''

    # Get the with music
    music = helper.extract_value_from_string_or_dict(elem, 'WFPlaylistItems')
    if music is None:
        music = ''

    # Get the author
    author = helper.extract_value_from_string_or_dict(elem, 'WFPlaylistAuthor')
    if author is None:
        author = ''

    # Get the comment
    comment = helper.extract_value_from_string_or_dict(elem, 'WFPlaylistDescription')
    if comment is None:
        comment = ''

    res = {'Create playlist': playlist, 'with': music, 'Author': author, 'Comment': comment}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
import parse_xml.parse_shortcut_WF as helper


def action_encodemedia(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Encode': '', 'Audio Only': False, 'Size': 'Passthrough', 'Speed': 'Normal', 'Title': '', 'Artist': '', 'Album': '', 'Genre': '', 'Year': '', 'Artwork': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # get what to encode
    encode_media = helper.extract_value_from_string_or_dict(elem, 'WFMedia')
    if encode_media is None:
        encode_media = ''

    # get audio only
    audio_only = helper.get_elements_after_key(elem, 'WFMediaAudioOnly', 'true')
    if audio_only is not None:
        audio_only = True
    else:
        audio_only = False

    res = {'Encode': encode_media, 'Audio Only': audio_only}

    if_aiff = False
    # if audio only is true, get the format
    if audio_only:
        audio_format = helper.extract_value_from_string_or_dict(elem, 'WFMediaAudioFormat')
        if audio_format is not None:
            res['Format'] = audio_format
        else:
            res['Format'] = 'M4A'

        if audio_format == 'AIFF':
            if_aiff = True
    else:
        # Get the size
        size = helper.extract_value_from_string_or_dict(elem, 'WFMediaSize')
        if size is not None:
            res['Size'] = size
        else:
            res['Size'] = 'Passthrough'
        # get preserve transparency if size is HEVC 1920x1080 or HEVC 3840x2160 or ProRes 422
        if size in ['HEVC 1920x1080', 'HEVC 3840x2160', 'ProRes 422']:
            preserve_transparency = helper.get_elements_after_key(elem, 'WFMediaPreserveTransparency', 'true')
            if preserve_transparency is not None:
                preserve_transparency = True
            else:
                preserve_transparency = False
            res['Preserve Transparency'] = preserve_transparency

    if not if_aiff:
        # get the speed
        speed = helper.extract_value_from_string_or_dict(elem, 'WFMediaSpeed')
        if speed is not None:
            res['Speed'] = speed
        else:
            res['Speed'] = 'Normal'

        # If speed is custom, get the custom speed
        if speed == 'Custom':
            custom_speed = helper.extract_value_from_string_or_dict(elem, 'WFMediaCustomSpeed')
            if custom_speed is not None:
                res['Custom Speed'] = custom_speed
            else:
                res['Custom Speed'] = '3'

    # Get the title
    title = helper.extract_value_from_string_or_dict(elem, 'WFMetadataTitle')
    if title is not None:
        res['Title'] = title
    else:
        res['Title'] = ''

    # Get the artist
    artist = helper.extract_value_from_string_or_dict(elem, 'WFMetadataArtist')
    if artist is not None:
        res['Artist'] = artist
    else:
        res['Artist'] = ''

    # Get the album
    album = helper.extract_value_from_string_or_dict(elem, 'WFMetadataAlbum')
    if album is not None:
        res['Album'] = album
    else:
        res['Album'] = ''

    # Get the genre
    genre = helper.extract_value_from_string_or_dict(elem, 'WFMetadataGenre')
    if genre is not None:
        res['Genre'] = genre
    else:
        res['Genre'] = ''

    # Get the year
    year = helper.extract_value_from_string_or_dict(elem, 'WFMetadataYear')
    if year is not None:
        res['Year'] = year
    else:
        res['Year'] = ''

    # Get the artwork
    artwork = helper.extract_value_from_string_or_dict(elem, 'WFMetadataArtwork')
    if artwork is not None:
        res['Artwork'] = artwork
    else:
        res['Artwork'] = ''

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
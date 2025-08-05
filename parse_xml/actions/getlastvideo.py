import parse_xml.parse_shortcut_WF as helper
import parse_xml_output.parse_output_to_natural_language as parse_output


def action_getlastvideo(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Get the latest': '1 video'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the number of videos
    number_of_videos = helper.extract_value_from_string_or_dict(elem, 'WFGetLatestPhotoCount')
    if number_of_videos is None:
        number_of_videos = '1 video'
    else:
        if type(number_of_videos) is list:
            number_of_videos = parse_output.parse_get_attachment(number_of_videos)
        number_of_videos = f'{number_of_videos} videos'

    res = {'Get the latest': number_of_videos}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
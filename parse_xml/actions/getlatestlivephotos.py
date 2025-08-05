import parse_xml.parse_shortcut_WF as helper
import parse_xml_output.parse_output_to_natural_language as parse_output

def action_getlatestlivephotos(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Get the latest': '1 live photo'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the number of live photos
    number_of_live_photos = helper.extract_value_from_string_or_dict(elem, 'WFGetLatestPhotoCount')
    if number_of_live_photos is None:
        number_of_live_photos = '1 live photo'
    else:
        if type(number_of_live_photos) is list:
            number_of_live_photos = parse_output.parse_get_attachment(number_of_live_photos)
        number_of_live_photos = f'{number_of_live_photos} live photos'

    res = {'Get the latest': number_of_live_photos}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
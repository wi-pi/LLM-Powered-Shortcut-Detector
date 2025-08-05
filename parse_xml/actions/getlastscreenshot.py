import parse_xml.parse_shortcut_WF as helper
import parse_xml_output.parse_output_to_natural_language as parse_output



def action_getlastscreenshot(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Get the latest': 'screenshot'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the number of screenshots
    number_of_screenshots = helper.extract_value_from_string_or_dict(elem, 'WFGetLatestPhotoCount')
    if number_of_screenshots is None:
        number_of_screenshots = 'screenshot'
    else:
        if type(number_of_screenshots) is list:
            number_of_screenshots = parse_output.parse_get_attachment(number_of_screenshots)
        number_of_screenshots = f'{number_of_screenshots} screenshots'

    res = {'Get the latest': number_of_screenshots}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
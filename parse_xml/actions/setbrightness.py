import parse_xml.parse_shortcut_WF as helper


def action_setbrightness(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Brightness': '0.5'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    if uuid is not None:
        raise ValueError('UUID is not None for brightness set')

    output_name = helper.track_custom_name(elem)


    # Get the brightness if action is Set
    brightness = helper.get_elements_after_key(elem, 'WFBrightness', 'real')
    if brightness is None:
        brightness = 0.5
    else:
        brightness = brightness[0].text

    res = {'Brightness': brightness}

    if output_name is not None:
        res['Output Name'] = output_name

    return helper.append_data(res, None)
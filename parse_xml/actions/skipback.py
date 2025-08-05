import parse_xml.parse_shortcut_WF as helper


def action_skipback(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Skip Back to the': 'Beginning', 'on': 'iPhone'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the position
    position = helper.extract_value_from_string_or_dict(elem, 'WFSkipBackBehavior')
    if position is None:
        position = 'Beginning'

    # Get the device
    device = helper.get_elements_after_key(elem, 'WFMediaRoute', 'dict')
    if device is not None:
        device_elem = helper.get_elements_after_key(device[0], 'routeName', 'string')
        if device_elem is not None:
            device = device_elem[0].text
        else:
            device = helper.extract_value_from_string_or_dict(elem, 'WFMediaRoute')
    else:
        device = 'iPhone'

    res = {'Skip Back to the': position, 'on': device}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
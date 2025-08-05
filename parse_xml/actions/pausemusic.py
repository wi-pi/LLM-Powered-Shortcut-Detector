import parse_xml.parse_shortcut_WF as helper
import parse_xml_output.parse_output_to_natural_language as output_helper


def action_pausemusic(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Play/Pause': '', 'on': 'iPhone'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the action
    action = helper.extract_value_from_string_or_dict(elem, 'WFPlayPauseBehavior')
    if action is None:
        action = 'Play/Pause'
    else:
        if type(action) == list:
            action = output_helper.parse_get_attachment(action)

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

    res = {action: '', 'on': device}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
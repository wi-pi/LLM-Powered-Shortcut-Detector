import parse_xml.parse_shortcut_WF as helper


def action_reboot(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Action': 'Shut Down'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    output_name = helper.track_custom_name(elem)

    # Get the action
    action = helper.extract_value_from_string_or_dict(elem, 'WFShutdownMode')
    if action is None:
        action = 'Shut Down'

    res = {'Action': action}

    if output_name is not None:
        res['Output Name'] = output_name

    return helper.append_data(res, uuid)
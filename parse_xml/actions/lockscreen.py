import parse_xml.parse_shortcut_WF as helper


def action_lockscreen(elem):
    if helper.check_validation(elem):
        raise ValueError('Invalid lockscreen')

    # Check UUID
    uuid = helper.track_uuid(elem)

    output_name = helper.track_custom_name(elem)

    if uuid is not None:
        raise ValueError('UUID is not None for lockscreen')

    res = {'Action': 'Lock the screen'}

    if output_name is not None:
        res['Output Name'] = output_name

    return helper.append_data(res, None)
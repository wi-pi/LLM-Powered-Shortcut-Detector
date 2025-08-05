import parse_xml.parse_shortcut_WF as helper


def action_appearance(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Action': 'Turn', 'Mode': 'Dark'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    if uuid is not None:
        raise ValueError('UUID is not None for appearance set')

    output_name = helper.track_custom_name(elem)

    # Get the action
    action = helper.extract_value_from_string_or_dict(elem, 'operation')
    if action is None:
        action = 'Turn'

    res = {'Action': action}

    # Get the mode if action is Turn
    if action == 'Turn':
        mode = helper.extract_value_from_string_or_dict(elem, 'style')
        if mode is None:
            mode = 'Dark'
        res['Mode'] = mode

    if output_name is not None:
        res['Output Name'] = output_name

    return helper.append_data(res, None)
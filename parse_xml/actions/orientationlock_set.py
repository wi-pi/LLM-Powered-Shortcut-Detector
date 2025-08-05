import parse_xml.parse_shortcut_WF as helper


def action_orientationlock_set(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Action': 'Toggle'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    if uuid is not None:
        raise ValueError('UUID is not None for personal hotspot set')

    output_name = helper.track_custom_name(elem)

    # Get the action
    action = helper.extract_value_from_string_or_dict(elem, 'operation')
    if action is None:
        action = 'Toggle'
    else:
        if action == 'set':
            action = 'Turn'

    res = {'Action': action}

    # Get the state if action is 'Turn'
    state = 'On'
    if action == 'Turn':
        state_elem = helper.get_elements_after_key(elem, 'OnValue', 'integer')
        if state_elem is not None:
            state_elem = state_elem[0].text
            if state_elem == '0':
                state = 'Off'
        res['State'] = state

    if output_name is not None:
        res['Output Name'] = output_name

    return helper.append_data(res, None)
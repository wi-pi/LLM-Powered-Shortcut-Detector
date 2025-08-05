import parse_xml.parse_shortcut_WF as helper


def action_flashlight(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Action': 'Turn', 'State': 'On', 'Brightness': '0.5'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    if uuid is not None:
        raise ValueError('UUID is not None for flashlight set')

    # Get the action
    action = helper.extract_value_from_string_or_dict(elem, 'operation')
    if action is None:
        action = 'Turn'

    res = {'Action': action}

    # Get the brightness
    brightness = helper.get_elements_after_key(elem, 'WFFlashlightLevel', 'real')
    if brightness is not None:
        brightness = brightness[0].text
    else:
        brightness = 0.5

    if_not_off = True

    # Get the state if action is 'Turn'
    state = 'On'
    if action == 'Turn':
        state_elem = helper.get_elements_after_key(elem, 'state', 'integer')
        if state_elem is not None:
            state_elem = state_elem[0].text
            if state_elem == '0':
                state = 'Off'
                if_not_off = False
        res['State'] = state

    if if_not_off:
        res['Brightness'] = brightness

    return helper.append_data(res, None)
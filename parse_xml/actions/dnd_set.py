import parse_xml.parse_shortcut_WF as helper


def action_dnd_set(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Action': 'Turn', 'Mode': 'Do Not Disturb', 'State': 'Off'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    if uuid is not None:
        raise ValueError('UUID is not None for dnd set')

    # Get the action
    action = helper.extract_value_from_string_or_dict(elem, 'Operation')
    if action is None:
        action = 'Turn'

    res = {'Action': action}

    # Get the mode
    mode = 'Do Not Disturb'
    mode_elem = helper.get_elements_after_key(elem, 'FocusModes', 'dict')
    if mode_elem is not None:
        display_elem = helper.get_elements_after_key(mode_elem[0], 'DisplayString', 'string')
        if display_elem is not None:
            mode = display_elem[0].text
        else:
            mode_elem = helper.get_final_value(mode_elem[0])
            mode = helper.get_attachments_by_range(mode_elem)

    res['Mode'] = mode

    # Get the state if action not 'Toggle'
    state = 'Off'
    if action == 'Turn':
        state_elem = helper.get_elements_after_key(elem, 'Enabled', 'integer')
        if state_elem is not None:
            state_elem = state_elem[0].text
            if state_elem == '1':
                state = 'On'
        res['State'] = state
        # Get the until time if state is 'On'
        if state == 'On':
            until_time = helper.extract_value_from_string_or_dict(elem, 'AssertionType')
            if until_time is None:
                until_time = 'Turned Off'
            res['Until'] = until_time

            # If until time is 'Event Ends', get the event name
            if until_time == 'Event Ends':
                event_name = helper.get_elements_after_key(elem, 'Event', 'dict')
                if event_name is not None:
                    event_name = helper.get_final_value(event_name[0])
                    event_name = helper.get_attachments_by_range(event_name)
                else:
                    event_name = ''
                res['Event Name'] = event_name
            elif until_time == 'Time':
                time = helper.extract_value_from_string_or_dict(elem, 'Time')
                if time is None:
                    time = ''
                res['Time'] = time

    return helper.append_data(res, uuid)
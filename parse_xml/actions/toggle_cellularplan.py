import parse_xml.parse_shortcut_WF as helper

def action_toggle_cellular_plan(elem):
    # Validate the input structure
    if not helper.check_validation(elem):
        return helper.append_data({'Action': 'Turn', 'State': 'On', 'Cellular plan': ''}, None)

    # Extract UUID
    uuid = helper.track_uuid(elem)

    # Extract the action
    action = helper.extract_value_from_string_or_dict(elem, 'operation')
    if action is None:
        action = 'Turn'

    res = {'Action': action}

    # Extract the state
    if action == 'Turn':
        state = helper.extract_value_from_string_or_dict(elem, 'state')
        if state is None or state == 1:
            state = 'On'
        else:
            state = 'Off'

        res['State'] = state

    # Extract the cellular plan
    cellular_plan = helper.extract_value_from_string_or_dict(elem, 'plan')
    if cellular_plan is None:
        cellular_plan = ''

    res['Cellular plan'] = cellular_plan

    return helper.append_data(res, uuid)

import parse_xml.parse_shortcut_WF as helper


def action_setting_autoanswer(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Turn': 'Auto Answer Calls On'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the operator
    operation = helper.extract_value_from_string_or_dict(elem, 'operation')
    if operation is None:
        operation = 'Turn'
    else:
        operation = helper.list_to_str(operation)

    autoanswer = 'Auto Answer Calls'
    if operation == 'Turn':
        state = helper.get_elements_after_key(elem, 'state', 'integer')
        if state is not None:
            if state[0] == 0:
                autoanswer = 'Auto Answer Calls Off'
            else:
                autoanswer = 'Auto Answer Calls On'
        else:
            autoanswer = 'Auto Answer Calls On'

    res = {operation: autoanswer}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
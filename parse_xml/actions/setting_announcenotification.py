import parse_xml.parse_shortcut_WF as helper


def action_setting_announcenotification(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Turn': 'Announce Notifications On'}, None)

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

    invert = 'Announce Notifications'
    if operation == 'Turn':
        state = helper.get_elements_after_key(elem, 'state', 'integer')
        if state is not None:
            if state[0] == 0:
                invert = 'Announce Notifications Off'
            else:
                invert = 'Announce Notifications On'
        else:
            invert = helper.extract_value_from_string_or_dict(elem, 'state')
            invert = helper.list_to_str(invert)
            if invert is None:
                invert = 'Announce Notifications On'

    res = {operation: invert}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
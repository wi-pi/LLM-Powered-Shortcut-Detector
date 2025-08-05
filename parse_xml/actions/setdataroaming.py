import parse_xml.parse_shortcut_WF as helper


def action_setdataroaming(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Turn': 'Data Roaming On', 'for': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    res = {}

    # Get the operator
    operation = helper.extract_value_from_string_or_dict(elem, 'operation')
    if operation is None:
        operation = 'Turn'
    else:
        operation = helper.list_to_str(operation)

    if operation == 'Turn':
        state = helper.get_elements_after_key(elem, 'state', 'integer')
        if state is not None:
            if state[0] == 0:
                res = {'Turn': 'Data Roaming Off'}
            else:
                res = {'Turn': 'Data Roaming On'}
        else:
            res = {'Turn': 'Data Roaming On'}
    else:
        res = {operation: 'Data Roaming'}

    # Get the carrier
    carrier = helper.get_elements_after_key(elem, 'plan', 'dict')
    if carrier is not None:
        carrier = helper.get_elements_after_key(carrier[0], 'title', 'dict')
        if carrier is None:
            carrier = helper.extract_value_from_string_or_dict(elem, 'plan')
        else:
            carrier = helper.extract_value_from_string_or_dict(carrier[0], 'key')
    if carrier is None:
        carrier = ''

    res['for'] = carrier

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
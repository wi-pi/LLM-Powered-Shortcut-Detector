import parse_xml.parse_shortcut_WF as helper


def action_setting_leftrightbalance(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Toggle': 'Left/Right Balance'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the type
    type = helper.extract_value_from_string_or_dict(elem, 'operation')
    if type is None:
        type = 'Toggle'
    else:
        type = helper.list_to_str(type)

    res = {type: 'Left/Right Balance'}

    if type == 'set':
        # Get the balance
        balance = helper.extract_value_from_string_or_dict(elem, 'value')
        if balance is None:
            balance = ''

        res['Balance'] = balance

        # Get the parameter
        parameter = helper.get_elements_after_key(elem, 'parameter', 'true')
        if parameter is not None:
            parameter = True
        else:
            parameter = False

        res['Parameter'] = parameter

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
import parse_xml.parse_shortcut_WF as helper


def action_setvariable(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Set variable': '', 'to': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the variable name
    variable_name = helper.get_elements_after_key(elem, 'WFVariableName', 'string')
    variable_name = '' if variable_name is None else variable_name[0].text

    # Get the variable value
    data = helper.extract_value_from_string_or_dict(elem, 'WFInput')
    if data is None:
        data = ''

    res = {'Set variable': variable_name, 'to': data}

    return helper.append_data(res, uuid)



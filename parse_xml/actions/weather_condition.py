import parse_xml.parse_shortcut_WF as helper


def action_weather_condition(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Get': '', 'from': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the detail
    detail = helper.extract_value_from_string_or_dict(elem, 'WFContentItemPropertyName')
    if detail is None:
        detail = ''

    # Get the weather
    weather = helper.extract_value_from_string_or_dict(elem, 'WFInput')
    if weather is None:
        weather = ''

    res = {'Get': detail, 'from': weather}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
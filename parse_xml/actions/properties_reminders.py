import parse_xml.parse_shortcut_WF as helper


def action_properties_reminders(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Get': '', 'from': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # Get what to get
    get = helper.extract_value_from_string_or_dict(elem, 'WFContentItemPropertyName')
    if get is None:
        get = ''

    # Get the subscribe
    subscribe = helper.extract_value_from_string_or_dict(elem, 'WFInput')
    if subscribe is None:
        subscribe = ''

    res = {'Get': get, 'from': subscribe}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name
    return helper.append_data(res, uuid)
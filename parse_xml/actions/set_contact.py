import parse_xml.parse_shortcut_WF as helper


def action_set_contact(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Action': 'Set', 'Detail': '', 'Contact': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    action = helper.extract_value_from_string_or_dict(elem, 'Mode')
    if action is None:
        action = 'Set'

    detail = helper.extract_value_from_string_or_dict(elem, 'WFContentItemPropertyName')
    if detail is None:
        detail = ''

    contact = helper.extract_value_from_string_or_dict(elem, 'WFContactContentItemLastName')
    if contact is None:
        contact = ''

    res = {'Action': action, 'Detail': detail, 'Contact': contact}

    if action == 'Set':
        to = helper.extract_value_from_string_or_dict(elem, 'WFInput')
        if to is None:
            to = ''

        res['To'] = to

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name
    return helper.append_data(res, uuid)
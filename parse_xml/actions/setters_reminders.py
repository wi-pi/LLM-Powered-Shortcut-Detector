import parse_xml.parse_shortcut_WF as helper


def action_setters_reminders(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Set': '', 'of': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    output_name = helper.track_custom_name(elem)

    # operation
    operation = helper.extract_value_from_string_or_dict(elem, 'Mode')
    if operation is None:
        operation = 'Set'
    else:
        operation = helper.list_to_str(operation)

    # detail
    detail = helper.extract_value_from_string_or_dict(elem, 'WFContentItemPropertyName')
    if detail is None:
        detail = ''

    # value
    value = helper.extract_value_from_string_or_dict(elem, 'WFInput')
    if value is None:
        value = ''

    res = {operation: detail, 'of': value}

    if operation == 'Set' and detail != '':
        to = helper.get_elements_after_key(elem, 'WFReminderContentItemTags', 'array')
        res_list = []
        if to is not None:
            for item in to[0]:
                res_list.append(helper.get_attachments_by_range(item))
        else:
            res_list = helper.extract_value_from_string_or_dict(elem, 'WFReminderContentItemTags')
        res['to'] = res_list

    if output_name is not None:
        res['Output Name'] = output_name

    return helper.append_data(res, uuid)
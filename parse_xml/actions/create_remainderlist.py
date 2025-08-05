import parse_xml.parse_shortcut_WF as helper


def action_create_remainderlist(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Reminders List Name': '', 'Parent Group': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    output_name = helper.track_custom_name(elem)

    reminder_list = helper.extract_value_from_string_or_dict(elem, 'name')
    if reminder_list is None:
        reminder_list = ''

    parent_group = helper.extract_value_from_string_or_dict(elem, 'group')
    if parent_group is None:
        parent_group = ''

    res = {'Reminders List Name': reminder_list, 'Parent Group': parent_group}

    if output_name is not None:
        res['Output Name'] = output_name

    return helper.append_data(res, uuid)
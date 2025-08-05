import parse_xml.parse_shortcut_WF as helper


def action_getupcomingreminders(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Get # of remainder': '1', 'from': 'All Lists'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the number of reminders
    num = helper.extract_value_from_string_or_dict(elem, 'WFGetUpcomingItemCount')
    if num is None:
        num = '1'

    # Get the list
    list = helper.get_elements_after_key(elem, 'WFGetUpcomingItemCalendar', 'dict')
    if list is not None:
        list = helper.extract_value_from_string_or_dict(list[0], 'Title')
        if list is None:
            list = helper.extract_value_from_string_or_dict(elem, 'WFGetUpcomingItemCalendar')
    if list is None:
        list = 'All Lists'

    res = {'Get # of remainder': num, 'from': list}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name
    return helper.append_data(res, uuid)
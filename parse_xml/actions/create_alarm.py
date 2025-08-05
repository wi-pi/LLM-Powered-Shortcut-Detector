import parse_xml.parse_shortcut_WF as helper


def action_create_alarm(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Create an Alarm for': '', 'called': 'Alarm', 'Repeat': '', 'Snooze': True}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output name if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the alarm time
    alarm_time = helper.extract_value_from_string_or_dict(elem, 'dateComponents')
    if alarm_time is None:
        alarm_time = ''

    # Get the create event name
    create_event_name = helper.extract_value_from_string_or_dict(elem, 'name')
    if create_event_name is None:
        create_event_name = 'Alarm'

    # Get the repeat input
    repeat_list = []
    repeat_elem = helper.get_elements_after_key(elem, 'repeats', 'array')
    if repeat_elem is not None:
        for item in repeat_elem[0]:
            repeat_list.append(helper.extract_value_from_string_or_dict(item, 'value'))
    else:
        repeat_list = helper.extract_value_from_string_or_dict(elem, 'repeats')

    # Get the snooze input
    snooze = helper.get_elements_after_key(elem, 'allowsSnooze', 'false')
    if snooze is None:
        snooze = True
    else:
        snooze = False

    res = {'Create ab Alarm for': alarm_time, 'called': create_event_name, 'Repeat': repeat_list, 'Snooze': snooze}

    if custom_output_name is not None:
        res['Custom output name'] = custom_output_name
    return helper.append_data(res, uuid)

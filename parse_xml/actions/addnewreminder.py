import parse_xml.parse_shortcut_WF as helper


def action_addnewreminder(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Add': '', 'to': 'Reminders', 'with': 'No Alert'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    output_name = helper.track_custom_name(elem)

    reminder_note = helper.extract_value_from_string_or_dict(elem, 'WFCalendarItemTitle')
    if reminder_note is None:
        reminder_note = ''


    to = helper.extract_value_from_string_or_dict(elem, 'WFCalendarItemCalendar')
    if to is None:
        to = 'Reminders'

    with_alert = helper.extract_value_from_string_or_dict(elem, 'WFAlertEnabled')
    if with_alert is None:
        with_alert = 'No Alert'

    res = {'Add': reminder_note, 'to': to, 'with': with_alert}

    if output_name is not None:
        res['Output Name'] = output_name

    return helper.append_data(res, uuid)
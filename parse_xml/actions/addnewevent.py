import parse_xml.parse_shortcut_WF as helper


def action_addnewevent(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Add': '', 'from': '', 'to': '', 'Location': '', 'Calendar': '', 'All Day': False, 'Alert': '', 'Notes': '', 'Show Compose Sheet': True}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the event name
    event_name = helper.extract_value_from_string_or_dict(elem, 'WFCalendarItemTitle')
    if event_name is None:
        event_name = ''

    # Get the from input
    from_input = helper.extract_value_from_string_or_dict(elem, 'WFCalendarItemStartDate')
    if from_input is None:
        from_input = ''

    # Get the to input
    to_input = helper.extract_value_from_string_or_dict(elem, 'WFCalendarItemEndDate')
    if to_input is None:
        to_input = ''

    # Get the location input
    location_input = helper.extract_value_from_string_or_dict(elem, 'WFCalendarItemLocation')
    if location_input is None:
        location_input = ''

    # Get the calendar input
    calendar_input = helper.get_elements_after_key(elem, 'WFCalendarDescriptor', 'dict')
    if calendar_input is None:
        calendar_input = ''
    else:
        cal_element = helper.extract_value_from_string_or_dict(calendar_input[0], 'Title')
        if cal_element is None:
            calendar_input = helper.extract_value_from_string_or_dict(elem, 'WFCalendarDescriptor')
            if calendar_input is None:
                calendar_input = ''
        else:
            calendar_input = cal_element

    # Get the all day input
    all_day_input = helper.get_elements_after_key(elem, 'WFCalendarItemAllDay', 'true')
    if all_day_input is None:
        all_day_input = False
    else:
        all_day_input = True

    # Get the alert input
    alert_input = helper.extract_value_from_string_or_dict(elem, 'WFAlertTime')
    if alert_input is None:
        alert_input = ''

    res = {'Add': event_name, 'from': from_input, 'to': to_input, 'Location': location_input, 'Calendar': calendar_input, 'All Day': all_day_input, 'Alert': alert_input}

    if alert_input == 'Custom':
        custom_time = helper.extract_value_from_string_or_dict(elem, 'WFAlertCustomTime')
        if custom_time is None:
            custom_time = ''
        res['Custom Time'] = custom_time

    # Get the notes input
    notes_input = helper.extract_value_from_string_or_dict(elem, 'WFCalendarItemNotes')
    if notes_input is None:
        notes_input = ''

    res['Notes'] = notes_input

    # Get the show compose sheet input
    show_compose_sheet_input = helper.get_elements_after_key(elem, 'ShowWhenRun', 'false')
    if show_compose_sheet_input is None:
        show_compose_sheet_input = True
    else:
        show_compose_sheet_input = False

    res['Show Compose Sheet'] = show_compose_sheet_input

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
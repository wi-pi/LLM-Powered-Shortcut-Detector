import parse_xml.parse_shortcut_WF as helper
import parse_xml_output.parse_output_to_natural_language as parse_output


def action_getupcomingevents(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Get': '1 event', 'from': 'All Calendars', 'Day': 'Any Day'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output name if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the number of event
    get_type = helper.extract_value_from_string_or_dict(elem, 'WFGetUpcomingItemCount')
    if get_type is None:
        get_type = '1 event'
    else:
        if type(get_type) == list:
            get_type = parse_output.parse_get_attachment(get_type)
        get_type = f"{get_type} event"

    # Get the calendar input
    calendar_input = helper.get_elements_after_key(elem, 'WFGetUpcomingItemCalendar', 'dict')
    if calendar_input is None:
        calendar_input = ''
    else:
        cal_element = helper.extract_value_from_string_or_dict(calendar_input[0], 'Title')
        if cal_element is None:
            calendar_input = helper.extract_value_from_string_or_dict(elem, 'WFGetUpcomingItemCalendar')
            if calendar_input is None:
                calendar_input = ''
        else:
            calendar_input = cal_element


    # Get the day input
    day_input = helper.extract_value_from_string_or_dict(elem, 'WFDateSpecifier')
    if day_input is None:
        day_input = 'Any Day'

    res = {'Get': get_type, 'from': calendar_input, 'Day': day_input}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
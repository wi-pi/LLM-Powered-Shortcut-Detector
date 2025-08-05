import parse_xml.parse_shortcut_WF as helper


def action_removeevents(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Remove': '', 'Include Future Events': False}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the calendar
    calendar = helper.extract_value_from_string_or_dict(elem, 'WFInputEvents')
    if calendar is None:
        calendar = ''

    # Get the include future events
    include_future_events = helper.get_elements_after_key(elem, 'WFCalendarIncludeFutureEvents', 'true')
    if include_future_events is None:
        include_future_events = False
    else:
        include_future_events = True

    res = {'Remove': calendar, 'Include Future Events': include_future_events}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
import parse_xml.parse_shortcut_WF as helper


def action_addnewcalendar(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Add new calendar': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the calendar
    calendar = helper.extract_value_from_string_or_dict(elem, 'CalendarName')
    if calendar is None:
        calendar = ''

    res = {'Add new calendar': calendar}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
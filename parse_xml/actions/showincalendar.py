import parse_xml.parse_shortcut_WF as helper
import parse_xml_output.parse_output_to_natural_language as parse_output


def action_showincalendar(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Open': ' in Calendar'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the calendar
    calendar = helper.extract_value_from_string_or_dict(elem, 'WFEvent')
    if calendar is None:
        calendar = ' in Calendar'
    else:
        if type(calendar) == list:
            calendar = parse_output.parse_get_attachment(calendar)
        calendar = f"{calendar} in Calendar"

    res = {'Open': calendar}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
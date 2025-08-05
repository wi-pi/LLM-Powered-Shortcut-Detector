import parse_xml.parse_shortcut_WF as helper
import parse_xml_output.parse_output_to_natural_language as parse_output



def action_setters_calendarevents(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Set': '', 'of': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the action type
    action_type = helper.extract_value_from_string_or_dict(elem, 'Mode')
    if action_type is None:
        action_type = 'Set'
    else:
        if type(action_type) == list:
            action_type = parse_output.parse_get_attachment(action_type)

    # Get the details
    details = helper.extract_value_from_string_or_dict(elem, 'WFContentItemPropertyName')
    if details is None:
        details = ''

    # Get the calendar
    calendar = helper.extract_value_from_string_or_dict(elem, 'WFInput')
    if calendar is None:
        calendar = ''

    res = {action_type: details , 'of': calendar}


    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
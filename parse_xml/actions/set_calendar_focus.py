import parse_xml.parse_shortcut_WF as helper
import parse_xml_output.parse_output_to_natural_language as parse_output


def action_set_calendar_focus(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Set': 'Calendar Focus Filter', 'while in': 'Do Not Disturb', 'Calendars':''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output name if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the set type input
    set_type = helper.extract_value_from_string_or_dict(elem, 'Mode')
    if set_type is None:
        set_type = 'Set'
    else:
        if type(set_type) == list:
            set_type = parse_output.parse_get_attachment(set_type)

    # Get the to input
    to_input = helper.get_elements_after_key(elem, 'FocusMode', 'dict')
    if to_input is None:
        to_input = 'Do Not Disturb'
    else:
        to_input = helper.extract_value_from_string_or_dict(to_input[0], 'DisplayString')
        if to_input is None:
            to_input = helper.extract_value_from_string_or_dict(elem, 'FocusMode')
        if to_input is None:
            to_input = 'Do Not Disturb'

    res = {set_type: 'Calendar Focus Filter', 'while in': to_input}


    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
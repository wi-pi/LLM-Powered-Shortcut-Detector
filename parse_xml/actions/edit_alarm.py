import parse_xml.parse_shortcut_WF as helper
import parse_xml_output.parse_output_to_natural_language as parse_output


def action_edit_alarm(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Skip': 'the next Sleep Alarm'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output name if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the alarm action
    alarm_action = helper.extract_value_from_string_or_dict(elem, 'operation')
    if alarm_action is None:
        alarm_action = 'Skip'
    else:
        if type(alarm_action) == list:
            alarm_action = parse_output.parse_get_attachment(alarm_action)

    res = {alarm_action: 'the next Sleep Alarm'}

    if custom_output_name is not None:
        res['Custom output name'] = custom_output_name
    return helper.append_data(res, uuid)
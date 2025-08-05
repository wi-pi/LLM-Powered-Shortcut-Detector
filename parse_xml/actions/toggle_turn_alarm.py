import parse_xml.parse_shortcut_WF as helper
import parse_xml_output.parse_output_to_natural_language as parse_output


def action_toggle_turn_alarm(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Turn': 'Alarm On', 'Show When Run': True}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output name if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the alarm action
    alarm_action = helper.extract_value_from_string_or_dict(elem, 'operation')
    if alarm_action is None:
        alarm_action = 'Turn'
    else:
        if type(alarm_action) == list:
            alarm_action = parse_output.parse_get_attachment(alarm_action)

    # Get the alarm time
    time_res = ''
    time = helper.get_elements_after_key(elem, 'alarm', 'dict')
    if time is not None:
        if len(time[0]) > 0:
            if time[0][0].text == 'identifier':
                time_elem = helper.get_elements_after_key(time[0], 'title', 'dict')
                time_res = helper.extract_value_from_string_or_dict(time_elem[0], 'key')
    else:
        time_res = helper.extract_value_from_string_or_dict(elem, 'alarm')
        if time_res is None:
            time_res = ''

    res = {alarm_action: f"Alarm {time_res}"}

    # Get the show when run
    show_when_run = helper.get_elements_after_key(elem, 'ShowWhenRun', 'false')
    if show_when_run is not None:
        show_when_run = False
    else:
        show_when_run = True

    res['Show When Run'] = show_when_run


    if custom_output_name is not None:
        res['Custom output name'] = custom_output_name
    return helper.append_data(res, uuid)
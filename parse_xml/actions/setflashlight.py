import parse_xml.parse_shortcut_WF as helper
import parse_xml_output.parse_output_to_natural_language as parse_output



def action_setflashlight(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Turn': 'Flashlight On', 'Show When Run': True}, None)

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

    invert = 'Flashlight'
    if alarm_action == 'Turn':
        state = helper.get_elements_after_key(elem, 'state', 'integer')
        if state is not None:
            if state[0] == 0:
                invert = 'Flashlight Off'
            else:
                invert = 'Flashlight On'
        else:
            invert = helper.extract_value_from_string_or_dict(elem, 'state')
            invert = helper.list_to_str(invert)
            if invert is None:
                invert = 'Flashlight On'

    # Get the show when run
    show_when_run = helper.get_elements_after_key(elem, 'ShowWhenRun', 'false')
    if show_when_run is not None:
        show_when_run = False
    else:
        show_when_run = True


    res = {alarm_action: invert, 'Show When Run': show_when_run}


    if custom_output_name is not None:
        res['Custom output name'] = custom_output_name
    return helper.append_data(res, uuid)
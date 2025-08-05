import parse_xml.parse_shortcut_WF as helper


def action_timer_start(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Start a Timer for': ' minutes'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output name if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the timer name
    timer = ''
    timer_elem = helper.get_elements_after_key(elem, 'WFDuration', 'dict')
    if timer_elem is not None:
        timer_name = helper.get_final_value(timer_elem[0])
        value = helper.extract_value_from_string_or_dict(timer_name, 'Magnitude')
        if value is None:
            value = ''
        unit = helper.extract_value_from_string_or_dict(timer_name, 'Unit')
        if unit is None:
            unit = ''
        timer = f"{value} {unit}"

    res = {'Start a Timer for': timer}




    if custom_output_name is not None:
        res['Output Name'] = custom_output_name
    return helper.append_data(res, uuid)
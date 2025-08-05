import parse_xml.parse_shortcut_WF as helper
import parse_xml_output.parse_output_to_natural_language as parse_output



def action_seek(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Seek': 'To Time', '30': 'seconds', 'on': 'iPhone'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # get what to seek
    seek = helper.extract_value_from_string_or_dict(elem, 'WFSeekBehavior')
    if seek is None:
        seek = 'To Time'

    # Get the time & unit
    time_elem = helper.get_elements_after_key(elem, 'WFTimeInterval', 'dict')
    if time_elem is not None:
        time_elem = helper.get_final_value(time_elem[0])
        time = helper.extract_value_from_string_or_dict(time_elem, 'Magnitude')
        if time is None:
            time = ''
        else:
            if type(time) == list:
                time = parse_output.parse_get_attachment(time)
        unit = helper.extract_value_from_string_or_dict(time_elem, 'Unit')
    else:
        time = '30'
        unit = 'seconds'

    # Get the device
    device = helper.get_elements_after_key(elem, 'WFMediaRoute', 'dict')
    if device is not None:
        device_elem = helper.get_elements_after_key(device[0], 'routeName', 'string')
        if device_elem is not None:
            device = device_elem[0].text
        else:
            device = helper.extract_value_from_string_or_dict(elem, 'WFMediaRoute')
    else:
        device = 'iPhone'

    # time_unit = time + ' ' + unit

    res = {'Seek': seek, time: unit, 'on': device}


    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
import parse_xml.parse_shortcut_WF as helper


def action_getdevicedetails(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Get Info': 'Device Name'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.get_elements_after_key(elem, 'CustomOutputName', 'string')
    if custom_output_name is not None:
        custom_output_name = custom_output_name[0].text

    # Get the device detail type
    device_detail_type = helper.extract_value_from_string_or_dict(elem, 'WFDeviceDetail')
    if device_detail_type is None:
        device_detail_type = 'Device Name'
    res = {'Get Info': device_detail_type}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name
    return helper.append_data(res, uuid)
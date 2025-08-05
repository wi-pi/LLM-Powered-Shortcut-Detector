import parse_xml.parse_shortcut_WF as helper


def action_getwifi(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Network': 'Wi-Fi', 'Info': 'Network Name'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.get_elements_after_key(elem, 'CustomOutputName', 'string')
    if custom_output_name is not None:
        custom_output_name = custom_output_name[0].text

    # Get the wifi or cellular or others
    network = helper.extract_value_from_string_or_dict(elem, 'WFNetworkDetailsNetwork')
    network = network if network is not None else 'Wi-Fi'

    res = {'Network': network}

    # Get the information you want to get
    if network == 'Wi-Fi':
        information = helper.extract_value_from_string_or_dict(elem, 'WFWiFiDetail')
        if information is None:
            res['Info'] = 'Network Name'
        else:
            res['Info'] = information
    elif network == 'Cellular':
        information = helper.extract_value_from_string_or_dict(elem, 'WFCellularDetail')
        if information is None:
            res['Info'] = 'Carrier Name'
        else:
            res['Info'] = information

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
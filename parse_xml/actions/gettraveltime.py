import parse_xml.parse_shortcut_WF as helper


def action_gettraveltime(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'From Location': '', 'To Location': '', 'Transport Mode': 'Driving'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output name if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the from location
    from_location = 'Current Location'
    from_location_elem = helper.get_elements_after_key(elem, 'WFGetDirectionsCustomLocation', 'dict')
    if from_location_elem is not None:
        from_location = helper.parse_location_wfinput(from_location_elem[0])

    # Get the to location
    to_location = ''
    to_location_elem = helper.get_elements_after_key(elem, 'WFDestination', 'dict')
    if to_location_elem is not None:
        to_location = helper.parse_location_wfinput(to_location_elem[0])

    # Get the transport mode
    transport_mode = 'Driving'
    transport_mode_elem = helper.extract_value_from_string_or_dict(elem, 'WFGetDirectionsActionMode')
    if transport_mode_elem is not None:
        transport_mode = transport_mode_elem

    res = {'From Location': from_location, 'To Location': to_location, 'Transport Mode': transport_mode}


    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
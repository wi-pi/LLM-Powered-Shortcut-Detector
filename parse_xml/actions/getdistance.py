import parse_xml.parse_shortcut_WF as helper


def action_getdistance(elem):
    if not helper.check_validation(elem):
        raise ValueError('Invalid Get Distance action')

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
    to_location_elem = helper.get_elements_after_key(elem, 'WFGetDistanceDestination', 'dict')
    if to_location_elem is not None:
        to_location = helper.parse_location_wfinput(to_location_elem[0])

    # Get the Route Type
    route_type = 'Direct'
    route_type_elem = helper.extract_value_from_string_or_dict(elem, 'WFGetDirectionsActionMode')
    if route_type_elem is not None:
        route_type = route_type_elem

    # Get the unit
    unit = 'Miles'
    unit_elem = helper.extract_value_from_string_or_dict(elem, 'WFDistanceUnit')
    if unit_elem is not None:
        unit = unit_elem

    # Get the precision
    precision = 'Nearest Hundred Meters'
    precision_elem = helper.extract_value_from_string_or_dict(elem, 'Accuracy')
    if precision_elem is not None:
        precision = precision_elem

    res = {'From Location': from_location, 'To Location': to_location, 'Route Type': route_type, 'Unit': unit, 'Precision': precision}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
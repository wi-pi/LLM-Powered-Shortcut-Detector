import parse_xml.parse_shortcut_WF as helper


def action_searchlocalbusinesses(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Find': '', 'Near': '', 'Radius': '1', 'Radius Unit': 'mile'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the search query
    search_query = helper.extract_value_from_string_or_dict(elem, 'WFSearchQuery')
    if search_query is None:
        search_query = ''

    # Get the location
    location = helper.get_elements_after_key(elem, 'WFInput', 'dict')
    if location is None:
        location = 'Current Location'
    else:
        if location[0][0].text == 'isCurrentLocation':
            location = 'Current Location'
        elif location[0][0].text != 'placemark':
            location = helper.extract_value_from_string_or_dict(elem, 'WFInput')
        else:
            location = helper.parse_location_wfinput(location[0])

    # Get the search radius
    radius = '1'
    unit_search = 'mile'
    radius_and_unit_elem = helper.get_elements_after_key(elem, 'WFSearchRadius', 'dict')
    if radius_and_unit_elem is not None:
        radius_and_unit_elem = helper.get_final_value(radius_and_unit_elem)
        radius = helper.extract_value_from_string_or_dict(radius_and_unit_elem, 'Magnitude')
        unit_search = helper.extract_value_from_string_or_dict(radius_and_unit_elem, 'Unit')

    res = {'Find': search_query, 'Near': location, 'Radius': radius, 'Radius Unit': unit_search}

    return helper.append_data(res, uuid)
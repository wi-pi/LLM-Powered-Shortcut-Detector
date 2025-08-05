import parse_xml.parse_shortcut_WF as helper


def action_gethalfwaypoint(elem):
    if not helper.check_validation(elem):
        raise ValueError('Invalid Get Halfway Point action')

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output name if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the from location
    from_location = ''
    from_location_elem = helper.get_elements_after_key(elem, 'WFGetHalfwayPointFirstLocation', 'dict')
    if from_location_elem is not None:
        from_location = helper.parse_location_wfinput(from_location_elem[0])

    # Get the to location
    to_location = ''
    to_location_elem = helper.get_elements_after_key(elem, 'WFGetHalfwayPointSecondLocation', 'dict')
    if to_location_elem is not None:
        to_location = helper.parse_location_wfinput(to_location_elem[0])

    res = {'Between': from_location, 'And': to_location}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
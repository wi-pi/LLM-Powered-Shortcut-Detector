import parse_xml.parse_shortcut_WF as helper


def action_getdirections(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Mode': 'Driving', 'Start': 'Current Location', 'End': '', 'App': 'Maps'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output name if have
    custom_output_name = helper.get_elements_after_key(elem, 'CustomOutputName', 'string')
    if custom_output_name is not None:
        custom_output_name = custom_output_name[0].text

    # Get the travel mode
    travel_mode = helper.extract_value_from_string_or_dict(elem, 'WFGetDirectionsActionMode')
    if travel_mode is None:
        travel_mode = 'Driving'

    # Get the start location
    start_location = helper.get_elements_after_key(elem, 'WFLocation', 'dict')
    if start_location is None:
        start_location = 'Current Location'
    else:
        if start_location[0][0].text != 'placemark':
            start_location = helper.extract_value_from_string_or_dict(elem, 'WFLocation')
        else:
            start_location = helper.parse_location_wfinput(start_location[0])

    # Get the end location
    end_location = helper.get_elements_after_key(elem, 'WFDestination', 'dict')
    if end_location is None:
        end_location = ''
    else:
        if end_location[0][0].text != 'placemark':
            end_location = helper.extract_value_from_string_or_dict(elem, 'WFDestination')
        else:
            end_location = helper.parse_location_wfinput(end_location[0])

    # Get the app
    app = helper.extract_value_from_string_or_dict(elem, 'WFGetDirectionsActionApp')
    if app is None:
        app = 'Maps'

    res = {'Mode': travel_mode, 'Start': start_location, 'End': end_location, 'App': app}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
import parse_xml.parse_shortcut_WF as helper


def action_weather_currentconditions(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Get current weather at': 'Current Location'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the location
    location = helper.get_elements_after_key(elem, 'WFWeatherCustomLocation', 'dict')
    if location is not None:
        location = helper.parse_location_wfinput(location[0])
    else:
        location = 'Current Location'


    res = {'Get current weather at': location}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)


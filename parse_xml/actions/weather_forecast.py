import parse_xml.parse_shortcut_WF as helper


def action_weather_forecast(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Get ': 'Daily forecast', 'at': 'Current Location'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the forecast
    forecast = helper.extract_value_from_string_or_dict(elem, 'WFWeatherForecastType')
    if forecast is None:
        forecast = 'Daily forecast'
    else:
        forecast = helper.list_to_str(forecast)
        forecast = f"{forecast} forecast"

    # Get the location
    location = helper.get_elements_after_key(elem, 'WFWeatherCustomLocation', 'dict')
    if location is not None:
        location = helper.parse_location_wfinput(location[0])
    else:
        location = 'Current Location'

    res = {'Get ': forecast, 'at': location}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
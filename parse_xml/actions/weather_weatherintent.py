import parse_xml.parse_shortcut_WF as helper


def action_weather_weatherintent(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Show weather in': 'My Location'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the location
    location = helper.get_elements_after_key(elem, 'location', 'dict')
    if location is not None:
        # try to find display name
        location = helper.extract_value_from_string_or_dict(location[0], 'displayString')
        if location is None:
            location = helper.extract_value_from_string_or_dict(elem, 'location')
    if location is None:
        location = 'My Location'

    res = {'Show weather in': location}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
import parse_xml.parse_shortcut_WF as helper


def action_properties_location(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Detail Type': '', 'Location': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Check if it has custom output name
    custom_output_name = helper.track_custom_name(elem)

    # Get the type of detail to fetch
    detail_type = helper.extract_value_from_string_or_dict(elem, 'WFContentItemPropertyName')
    if detail_type is None:
        detail_type = ''

    res = {'Detail Type': detail_type}

    # the location to get the detail
    location = helper.extract_value_from_string_or_dict(elem, 'WFInput')
    if location is None:
        location = ''

    res['Location'] = location

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
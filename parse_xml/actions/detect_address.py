import parse_xml.parse_shortcut_WF as helper


def action_detect_address(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Get addresses from': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output name if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the location
    location = ''
    location_elem = helper.extract_value_from_string_or_dict(elem, 'WFInput')
    if location_elem is not None:
        location = location_elem

    res = {'Get addresses from': location}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
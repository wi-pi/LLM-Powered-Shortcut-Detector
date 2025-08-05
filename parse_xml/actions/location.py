import parse_xml.parse_shortcut_WF as helper


def action_location(elem):
    if not helper.check_validation(elem):
        raise ValueError('Invalid Location action')

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output name if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the location
    location = ''
    location_elem = helper.get_elements_after_key(elem, 'WFLocation', 'dict')
    if location_elem is not None:
        location = helper.parse_location_wfinput(location_elem[0])

    res = {'Location': location}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
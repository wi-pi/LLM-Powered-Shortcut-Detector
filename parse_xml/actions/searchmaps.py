import parse_xml.parse_shortcut_WF as helper


def action_searchmap(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Location': '', 'App': 'Maps'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output name if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the search query
    search_query = helper.get_elements_after_key(elem, 'WFInput', 'dict')
    if search_query is None:
        search_query = ''
    else:
        if search_query[0][0].text == 'isCurrentLocation':
            search_query = 'Current Location'
        else:
            if search_query[0][0].text != 'placemark':
                search_query = helper.extract_value_from_string_or_dict(elem, 'WFInput')
            else:
                search_query = helper.parse_location_wfinput(search_query[0])

    # Get the app
    app = helper.extract_value_from_string_or_dict(elem, 'WFSearchMapsActionApp')
    if app is None:
        app = 'Maps'

    res = {'Location': search_query, 'App': app}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
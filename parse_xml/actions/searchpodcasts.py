import parse_xml.parse_shortcut_WF as helper
import parse_xml_output.parse_output_to_natural_language as output_helper



def action_searchpodcasts(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Find': ' on Apple Podcasts', 'Search By': 'All', 'Results': 'Podcasts', 'Country': 'United States', 'Get Items': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output name if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the search input
    search = helper.extract_value_from_string_or_dict(elem, 'WFSearchTerm')
    if search is None:
        search = ''
    else:
        if type(search) is list:
            search = output_helper.parse_get_attachment(search)

    # Get the search by
    search_by = helper.extract_value_from_string_or_dict(elem, 'WFAttribute')
    if search_by is None:
        search_by = 'All'

    res = {'Find': f" {search} on Apple Podcasts", 'Search By': search_by}

    # Get the results if search by is not product id
    if search_by != 'Product ID':
        results = helper.extract_value_from_string_or_dict(elem, 'WFEntity')
        if results is None:
            results = 'Podcasts'
        res['Results'] = results

    # Get the country
    country = helper.extract_value_from_string_or_dict(elem, 'WFCountry')
    if country is None:
        country = 'United States'

    res['Country'] = country

    # Get the get items if search by is not product id
    if search_by != 'Product ID':
        get_items = helper.extract_value_from_string_or_dict(elem, 'WFItemLimit')
        if get_items is None:
            get_items = ''
        res['Get Items'] = get_items

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
import parse_xml.parse_shortcut_WF as helper
import parse_xml_output.parse_output_to_natural_language as parse_output


def action_searchappstore(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Find': ' on the App Store', 'Search By': 'All', 'Results': 'iPhone', 'Region': 'United States', 'Get Items': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the search
    search = helper.extract_value_from_string_or_dict(elem, 'WFSearchTerm')
    if search is None:
        search = ' on the App Store'
    else:
        if type(search) == list:
            search = parse_output.parse_get_attachment(search)
        search = f" '{search}' on the App Store"

    # Get the search by
    search_by = helper.extract_value_from_string_or_dict(elem, 'WFAttribute')
    if search_by is None:
        search_by = 'All'

    res = {'Find': search, 'Search By': search_by}

    if search_by != 'Product ID':
        # Get the results
        result = helper.extract_value_from_string_or_dict(elem, 'WFEntity')
        if result is None:
            result = 'iPhone'

        res['Results'] = result

    # Get the region
    region = helper.extract_value_from_string_or_dict(elem, 'WFCountry')
    if region is None:
        region = 'United States'

    res['Region'] = region

    if search_by != 'Product ID':
        # Get the get items
        get_items = helper.extract_value_from_string_or_dict(elem, 'WFItemLimit')
        if get_items is None:
            get_items = ''

        res['Get Items'] = get_items
    
    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
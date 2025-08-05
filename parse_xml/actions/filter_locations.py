import parse_xml.parse_shortcut_WF as helper
from parse_xml.actions.conditional import condition_map
from parse_xml_output.parse_output_to_natural_language import parse_get_attachment

def action_filter_locations(elem):
    if not helper.check_validation(elem):
        raise ValueError('Invalid Filter Locations action')

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the location
    location_input = helper.extract_value_from_string_or_dict(elem, 'WFContentItemInputParameter')
    if location_input is None:
        location_input = ''

    res = {'Location Input': location_input}

    # Get the filters
    filter_list = []
    get_elem = helper.get_elements_after_key(elem, 'WFContentItemFilter', 'dict')
    if get_elem is not None:
        get_elem = helper.get_final_value(get_elem[0])
        filters_array = helper.get_elements_after_key(get_elem, 'WFActionParameterFilterTemplates', 'array')
        if filters_array is not None:
            filters_array = helper.get_final_value(filters_array[0])
            for filter_elem in filters_array:
                # Get the condition item
                condition_item = helper.get_elements_after_key(filter_elem, 'Operator', 'integer')
                if condition_item is None:
                    raise ValueError('Condition item not found for Filter Locations')
                compare_num = helper.extract_value(condition_item[0])
                condition_item = condition_map[compare_num]
                # Get data A
                data_a = helper.extract_value_from_string_or_dict(filter_elem, 'Property')
                if data_a is None:
                    raise ValueError('Data A not found for Filter Locations')
                # Get data B
                data_b = ''
                data_b_dict = helper.get_elements_after_key(filter_elem, 'Values','dict')
                if data_b_dict is not None and len(data_b_dict[0]) > 0:
                    # Get the type of value
                    if data_b_dict[0][0].tag != 'key':
                        raise ValueError('Data B not found for Filter Locations')
                    element_type = data_b_dict[0][0].text
                    data_b_dict = data_b_dict[0][1]
                    if element_type == 'Number' or element_type == 'Enumeration':
                        data_b = helper.extract_value_from_string_or_dict(data_b_dict, 'Value')
                        if data_b is None:
                            data_b = ''
                    elif element_type == 'String':
                        elem_cur = helper.get_final_value(data_b_dict)
                        data_b = helper.get_attachments_by_range(elem_cur)
                    else:
                        raise ValueError('Data B not found for Filter Locations -- Unknown')
                data_b = parse_get_attachment(data_b)
                filter_list.append(f"{data_a} {condition_item} {data_b}")
        # Get the conjunction
        conjunction = helper.get_elements_after_key(get_elem, 'WFActionParameterFilterPrefix', 'integer')
        if conjunction is None:
            raise ValueError('Conjunction not found for Filter Locations')
        conjunction = helper.extract_value(conjunction[0])
        conjunction = 'Any of the following are true' if conjunction == 0 else 'All of the following are true'
        res['Condition'] = conjunction

    res['Filters'] = filter_list

    # Get the Sort By item
    sort_property = helper.extract_value_from_string_or_dict(elem, 'WFContentItemSortProperty')
    if sort_property is None:
        sort_property = 'None'
    res['Sort By'] = sort_property

    # Get the Sort Order
    if sort_property != 'None' and sort_property != 'Random':
        sort_order = helper.extract_value_from_string_or_dict(elem, 'WFContentItemSortOrder')
        if sort_order is None:
            raise ValueError('Sort Order not found for Filter Locations')
        res['Order'] = sort_order

    # Get the Limit
    limit_enable = False
    limit_elem = helper.get_elements_after_key(elem, 'WFContentItemLimitEnabled', 'true')
    if limit_elem is not None:
        limit_enable = True
    res['Limit'] = limit_enable

    # Get the Limit Count if enabled
    if limit_enable:
        limit_count = helper.get_elements_after_key(elem, 'WFContentItemLimitNumber', 'real')
        if limit_count is None:
            limit_count = 5
        else:
            limit_count = helper.extract_value(limit_count[0])
        res['Limit Count'] = limit_count

    return helper.append_data(res, uuid)
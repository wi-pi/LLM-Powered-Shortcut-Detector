import parse_xml.parse_shortcut_WF as helper
from parse_xml.actions.conditional import condition_map

date_unit = {
    4: 'years',
    8: 'months',
    8192: 'weeks',
    16: 'days'
}

def action_filter_articles(elem):
    if not helper.check_validation(elem):
        raise ValueError('Invalid Filter Files action')

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the from input
    from_input = helper.extract_value_from_string_or_dict(elem, 'WFContentItemInputParameter')
    if from_input is None:
        from_input = ''

    res = {'Filter': from_input}

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
                    raise ValueError('Condition item not found for Filter article')
                compare_num = helper.extract_value(condition_item[0])
                condition_item = condition_map[compare_num]
                # Get data A
                data_a = helper.extract_value_from_string_or_dict(filter_elem, 'Property')
                if data_a is None:
                    raise ValueError('Data A not found for Filter article')
                # Get data B
                data_b = ''
                data_b_dict_inter = helper.get_elements_after_key(filter_elem, 'Values', 'dict')
                if data_b_dict_inter is not None and len(data_b_dict_inter[0]) > 0:
                    # Get the type of value
                    if data_b_dict_inter[0][0].tag != 'key':
                        raise ValueError('Data B not found for Filter article')
                    element_type = data_b_dict_inter[0][0].text
                    data_b_dict = data_b_dict_inter[0][1]
                    if element_type == 'Number' or element_type == 'Enumeration':
                        data_b = helper.extract_value_from_string_or_dict(data_b_dict, 'Value')
                        if data_b is None:
                            data_b = ''
                    elif element_type == 'String':
                        elem_cur = helper.get_final_value(data_b_dict)
                        data_b = helper.get_attachments_by_range(elem_cur)
                        if data_b is None:
                            data_b = ''
                    elif element_type == 'Date':
                        elem_cur = helper.get_final_value(data_b_dict)
                        data_b = helper.get_attachments_by_range(elem_cur)
                        if data_b is None:
                            data_b = ''
                    elif element_type == 'AnotherDate':
                        elem_cur = helper.get_final_value(data_b_dict)
                        data_b = helper.get_attachments_by_range(elem_cur)
                        if data_b is None:
                            data_b = ''
                        if compare_num != 1003:
                            raise ValueError('Data C error')
                        data_c = helper.get_elements_after_key(data_b_dict_inter[0], 'Date', 'dict')
                        if data_c is None:
                            data_c = ''
                        else:
                            data_c = helper.get_final_value(data_c[0])
                            data_c = helper.get_attachments_by_range(data_c)
                            if data_c is None:
                                data_c = ''
                        data_b = f"{data_b} and {data_c}"
                    elif element_type == 'Unit':
                        if compare_num == 1002:
                            data_b = 'is today'
                        data_b = ''
                    else:
                        raise ValueError('Data B not found for Filter article -- Unknown')
                if compare_num in [1001, 1000]:
                    unit = helper.get_elements_after_key(data_b_dict_inter[0], 'Unit', 'dict')
                    if unit is not None:
                        unit = helper.get_elements_after_key(unit[0], 'Value', 'integer')
                        unit = helper.extract_value(unit[0])
                        data_b = f"{data_b} {date_unit[unit]}"
                    else:
                        raise ValueError('Unit not found for Filter article')
                filter_list.append(f"{data_a} {condition_item} {data_b}")
        # Get the conjunction
        conjunction = helper.get_elements_after_key(get_elem, 'WFActionParameterFilterPrefix', 'integer')
        if conjunction is None:
            raise ValueError('Conjunction not found for Filter Locations')
        conjunction = helper.extract_value(conjunction[0])
        conjunction = 'Any of the following are true' if conjunction == 0 else 'All of the following are true'
        res['Condition'] = conjunction

    res['Filter List'] = filter_list

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

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
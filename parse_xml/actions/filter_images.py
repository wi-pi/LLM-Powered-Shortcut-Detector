import parse_xml.parse_shortcut_WF as helper
from parse_xml.actions.conditional import condition_map

date_unit = {
    4: 'years',
    8: 'months',
    16: 'weeks',
    8192: 'days',
    128: 'seconds',
    32: 'hours',
    64: 'minutes'
}

file_unit_code = {
    1: 'bytes',
    2: 'KB',
    4: 'MB',
    8: 'GB',
    16: 'TB',
    32: 'PB',
    64: 'EB',
    128: 'ZB'
}

def action_filter_images(elem):
    if not helper.check_validation(elem):
        raise ValueError('Invalid Filter Image action')

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
                condition_item = condition_map.get(compare_num, 'Unknown')

                # Get data A
                data_a = helper.extract_value_from_string_or_dict(filter_elem, 'Property')
                if data_a is None:
                    raise ValueError('Data A not found for Filter article')

                # Get data B

                data_b = ''
                data_b_dict_inter = helper.get_elements_after_key(filter_elem, 'Values', 'dict')
                if data_b_dict_inter is not None and len(data_b_dict_inter[0]) > 0:
                    filtered_data_b_dict = []
                    # Check if the specific 'Number' element with the matching value needs to be ignored
                    i = 0
                    removed_bool = False
                    while i < len(data_b_dict_inter[0]):
                        element = data_b_dict_inter[0][i]

                        # Check if the current element is a <key> and its text is 'Number'
                        if element.text == 'Number':
                            # Access the associated <dict> that follows the <key>
                            number_dict = data_b_dict_inter[0][i + 1]
                            value = helper.extract_value_from_string_or_dict(number_dict, 'Value')
                            # Remove the exact match of <Number><Value>300</Value><WFSerializationType>WFNumberStringSubstitutableState</WFSerializationType>
                            if value == '300':
                                # Only skip (remove) if there are more than two items in data_b_dict_inter[0]
                                if len(data_b_dict_inter[0]) > 2:
                                    # Skip the <key> and its associated <dict>
                                    i += 2
                                    removed_bool = True
                                    continue

                        # If no condition was met, add the element to the filtered list
                        filtered_data_b_dict.append(element)
                        i += 1

                    element_type = filtered_data_b_dict[0].text
                    data_b_dict = filtered_data_b_dict[1]
                    data_b = '300'

                    if element_type == 'ByteCountUnit':
                        # Get the value
                        value_here = helper.get_elements_after_key(filtered_data_b_dict, 'Number', 'dict')
                        if value_here is not None:
                            value_here = helper.get_final_value(value_here[0])
                            value_here = helper.get_attachments_by_range(value_here)
                        if value_here is None and removed_bool:
                            value_here = '300'
                        else:
                            value_here = helper.extract_value_from_string_or_dict(filtered_data_b_dict, 'Number')
                            if value_here is None:
                                value_here = ''
                        # Get the unit
                        unit_here = helper.get_elements_after_key(filtered_data_b_dict, 'ByteCountUnit', 'dict')
                        if unit_here is not None:
                            unit_here = helper.get_final_value(unit_here[0])
                            unit_here = helper.get_attachments_by_range(unit_here)
                        else:
                            unit_here = helper.get_elements_after_key(filtered_data_b_dict, 'ByteCountUnit', 'integer')
                            if unit_here is not None:
                                unit_here = helper.extract_value(unit_here[0])
                            else:
                                raise ValueError('Unit not found for Filter image')
                        if type(unit_here) is not list:
                            # used code to denote the unit
                            code = int(unit_here)
                            unit_here = file_unit_code[code]
                        if unit_here is None: unit_here = ''
                        data_b = f"{value_here} {unit_here}"

                    elif data_a == 'Duration':
                        # Get the value
                        value_here = helper.get_elements_after_key(filtered_data_b_dict, 'Number', 'dict')
                        if value_here is not None:
                            value_here = helper.get_final_value(value_here[0])
                            value_here = helper.get_attachments_by_range(value_here)
                        else:
                            if removed_bool:
                                value_here = '300'
                            else:
                                value_here = ''
                        # Get the unit
                        unit_here = helper.get_elements_after_key(filtered_data_b_dict, 'Unit', 'dict')
                        unit_here = helper.get_final_value(unit_here[0])
                        unit_here = helper.get_attachments_by_range(unit_here)
                        if type(unit_here) is not list:
                            # used code to denote the unit
                            code = int(unit_here)
                            unit_here = date_unit[code]
                        if unit_here is None: unit_here = ''
                        data_b = f"{value_here} {unit_here}"

                    elif element_type in ['Number', 'Enumeration']:
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
                        data_c = helper.get_elements_after_key(filtered_data_b_dict, 'Date', 'dict')
                        if data_c is not None:
                            data_c = helper.get_final_value(data_c[0])
                            data_c = helper.get_attachments_by_range(data_c)
                        else:
                            data_c = ''
                        data_b = f"{data_b} and {data_c}"

                    elif element_type == 'Bool':
                        bool_val = helper.get_elements_after_key(data_b_dict, 'Value', 'true')
                        condition_item = 'is'
                        if bool_val is not None:
                            data_b = 'true'
                        else:
                            data_b = 'false'

                    else:
                        raise ValueError('Data B not found for Filter article -- Unknown')

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
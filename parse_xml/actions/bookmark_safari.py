import parse_xml.parse_shortcut_WF as helper
from parse_xml.actions.conditional import condition_map
import parse_xml_output.parse_output_to_natural_language as parse_output

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

def action_bookmark_safari(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Find': 'All BookMark', 'Condition': 'All of the following are true', 'Filter List': ['Type is Steps', 'Start Date is in the last 7 days'], 'Unit': 'count', 'Group by': 'None','Sort by': 'None', 'Limit': False}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    input_text = helper.extract_value_from_string_or_dict(elem, 'WFContentItemInputParameter')
    if input_text is None:
        input_text = 'All BookMark'

    res = {'Filter': input_text}

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
                if data_b_dict_inter is None:
                    data_b = ''
                    filter_list.append(f"{data_a} {condition_item} {data_b}")
                    continue

                # Get the type of value
                if len(data_b_dict_inter[0]) == 0:
                    data_b = ''
                    filter_list.append(f"{data_a} {condition_item} {data_b}")
                    continue
                element_type = data_b_dict_inter[0][0].text
                data_b_dict = data_b_dict_inter[0][1]
                data_b_dict_inter = data_b_dict_inter[0]

                if element_type == 'ByteCountUnit':
                    # Get the value
                    value_here = helper.get_elements_after_key(data_b_dict_inter, 'Number', 'dict')
                    if value_here is not None:
                        value_here = helper.get_final_value(value_here[0])
                        value_here = helper.get_attachments_by_range(value_here)
                    else:
                        value_here = helper.extract_value_from_string_or_dict(data_b_dict_inter, 'Number')
                        if value_here is None:
                            value_here = ''
                    # Get the unit
                    unit_here = helper.get_elements_after_key(data_b_dict_inter, 'ByteCountUnit', 'dict')
                    if unit_here is not None:
                        unit_here = helper.get_final_value(unit_here[0])
                        unit_here = helper.get_attachments_by_range(unit_here)
                    else:
                        unit_here = helper.get_elements_after_key(data_b_dict_inter, 'ByteCountUnit',
                                                                  'integer')
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
                    value_here = helper.get_elements_after_key(data_b_dict_inter, 'Number', 'dict')
                    if value_here is not None:
                        value_here = helper.get_final_value(value_here[0])
                        value_here = helper.get_attachments_by_range(value_here)
                    else:
                        value_here = ''
                    # Get the unit
                    unit_here = helper.get_elements_after_key(data_b_dict_inter, 'Unit', 'dict')
                    if unit_here is None:
                        unit_here = helper.get_elements_after_key(data_b_dict_inter, 'Unit', 'integer')
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
                    # if compare_num != 1003:
                    #     raise ValueError('Data C error')
                    data_c = helper.get_elements_after_key(data_b_dict_inter, 'Date', 'dict')
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

                elif element_type == 'Unit':
                    data_b = ''
                else:
                    raise ValueError('Data B not found for Filter article -- Unknown')
                if compare_num in [1001, 1000]:
                    unit_elem = helper.get_elements_after_key(data_b_dict_inter, 'Unit', 'dict')
                    if unit_elem is not None:
                        unit = helper.get_elements_after_key(unit_elem[0], 'Value', 'integer')
                        if unit is not None:
                            unit = helper.extract_value(unit[0])
                        else:
                            unit = helper.extract_value_from_string_or_dict(unit_elem[0], 'Value')
                        if type(unit) is list:
                            unit = parse_output.parse_get_attachment(unit)
                            data_b = f"{data_b} {unit}"
                        else:
                            data_b = f"{data_b} {date_unit[unit]}"
                    # else:
                    #     raise ValueError('Unit not found for Filter article')
                filter_list.append(f"{data_a} {condition_item} {data_b}")

        # Get the conjunction
        conjunction = helper.get_elements_after_key(get_elem, 'WFActionParameterFilterPrefix', 'integer')
        if conjunction is None:
            raise ValueError('Conjunction not found for Filter Locations')
        conjunction = helper.extract_value(conjunction[0])
        conjunction = 'Any of the following are true' if conjunction == 0 else 'All of the following are true'
        res['Condition'] = conjunction

    res['Filter List'] = filter_list

    # Get the Unit
    unit = helper.extract_value_from_string_or_dict(elem, 'WFHKSampleFilteringUnit')
    if unit is None:
        unit = ''
    res['Unit'] = unit

    # Get the Group By item
    group_by = helper.extract_value_from_string_or_dict(elem, 'WFHKSampleFilteringGroupBy')
    if group_by is None:
        group_by = 'None'

    res['Group By'] = group_by

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
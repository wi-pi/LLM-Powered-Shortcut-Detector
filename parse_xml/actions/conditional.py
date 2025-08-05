import parse_xml.parse_shortcut_WF as helper

condition_map = {
    100: 'has any value',
    101: 'does not have any value',
    0: 'is before/less than',
    1: 'is less than or equal to',
    2: 'is after/greater than',
    3: 'is greater than or equal to',
    4: 'is',
    5: 'is not',
    9: 'ends with',
    8: 'begins with',
    999: 'does not contain',
    99: 'contains',
    1000: 'is in the next',
    1001: 'is in the last',
    1002: 'is today',
    1003: 'is between',
    None: 'is exactly',
}

def check_data_B(elem, compare_num):
    # Check on data (B)
    # Special case for 1003
    if compare_num == 1003:
        A, B = '', ''
        i = 0
        find = 0
        while i < len(elem) -1:
            if elem[i].tag == 'key' and elem[i].text == 'WFNumberValue':
                if find == 0:
                    A = helper.extract_value(elem[i+1])
                elif find == 1:
                    B = helper.extract_value(elem[i+1])
                find += 1
                if find == 2:
                    break
            elif elem[i].tag == 'key' and elem[i].text == 'WFDate':
                if find == 0:
                    A = helper.extract_value(elem[i+1])
                elif find == 1:
                    B = helper.extract_value(elem[i+1])
                find += 1
                if find == 2:
                    break
            i += 1
        return f"{A} and {B}"
    # case 1 there is a string
    compared_to = helper.get_elements_after_key(elem, 'WFConditionalActionString', 'string')
    if compared_to is not None:
        return compared_to[0].text
    # case 2 there is a dictionary
    compared_to = helper.get_elements_after_key(elem, 'WFConditionalActionString', 'dict')
    if compared_to is not None:
        compared_to = helper.get_final_value(compared_to[0])
        return helper.get_attachments_by_range(compared_to)
    # case 3 there is a date
    compared_to = helper.get_elements_after_key(elem, 'WFDate', 'date')
    if compared_to is not None:
        return helper.extract_value(compared_to[0])
    # case 4 there is a number
    if compare_num in [0, 1, 2, 3, 4, 5]:
        compared_to = helper.get_elements_after_key(elem, 'WFNumberValue', 'string')
        if compared_to is not None:
            return compared_to[0].text

    return None


def action_conditional(elem):
    if not helper.check_validation(elem):
        raise ValueError('Invalid Conditional action')
    # Check UUID
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.get_elements_after_key(elem, 'CustomOutputName', 'string')
    if custom_output_name is not None:
        custom_output_name = custom_output_name[0].text

    metadata_list = {}
    # Track the Group Identifier
    group_identifier = helper.get_metadata(elem, 'GroupingIdentifier')
    if group_identifier is None:
        raise ValueError('GroupingIdentifier is not found in the conditional action.')
    metadata_list['Group Identifier'] = group_identifier
    # Track the control Type
    condition_type = helper.get_metadata(elem, 'WFControlFlowMode')
    if condition_type is None:
        raise ValueError('WFControlFlowMode is not found in the conditional action.')
    if condition_type == 0:
        metadata_list['Action'] = 'If'
    elif condition_type == 1:
        metadata_list['Action'] = 'Otherwise'
        return {'metadata': metadata_list}, {'uuid': uuid}
    elif condition_type == 2:
        metadata_list['Action'] = 'End If'
        if custom_output_name is not None:
            metadata_list['Output Name'] = custom_output_name
        return {'metadata': metadata_list}, {'uuid': uuid}
    else:
        raise ValueError('WFControlFlowMode has an unexpected value in the conditional action.')

    # Check on condition data
    condition_data = helper.get_elements_after_key(elem, 'WFCondition', 'integer')
    # if condition_data is None:
    #     raise ValueError('WFCondition is not found in the conditional action.')
    if condition_data is not None:
        condition_data = helper.extract_value(condition_data[0])
    # Comparing A condition B
    A = ''
    condition_between = condition_map[condition_data]
    B = ''
    # Check on data (A)
    data = helper.get_elements_after_key(elem, 'WFInput', 'dict')
    if data is not None:
        res_dict = helper.get_all_dicts_at_depth_n(data[0], 1)
        res_dict = helper.get_final_value(res_dict[0])
        A = helper.get_attachments_by_range(res_dict)
    B = check_data_B(elem, condition_data)
    if B is None:
        B = ''
    if condition_data == 4 and A is not None and B == '':
        return {'metadata': metadata_list}, helper.append_data(f"{A}", uuid)
    return {'metadata': metadata_list}, helper.append_data_interface(A, B, uuid, 'action_conditional', condition_between)


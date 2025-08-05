import parse_xml.parse_shortcut_WF as helper

def recursive_dict(elem, key_or_value, results=None, flat=False):
    if results is None:
        results = []

    if flat:
        elem = helper.get_final_value(elem)
    else:
        elems = helper.get_elements_after_key(elem, key_or_value, 'dict')
        if elems is None:
            if len(results) == 0:
                return ''
            return results  # Return the accumulated results so far

        elem = helper.get_final_value(elems[0])

    if elem.tag == 'dict':
        items_array = helper.get_elements_after_key(elem, 'WFDictionaryFieldValueItems', 'array')
        if not items_array:
            # No 'WFDictionaryFieldValueItems' key, try to extract value directly
            return helper.get_attachments_by_range(elem)
        else:
            # 'WFDictionaryFieldValueItems' exists, so it's a nested dictionary
            items = list(items_array[0])
            for item in items:
                # Recursively extract key and value using separate temporary lists
                key_results = []
                value_results = []
                key = recursive_dict(item, 'WFKey', key_results)
                value = recursive_dict(item, 'WFValue', value_results)
                # Create a new dictionary with the key-value pair
                new_dict = {'key': key, 'value': value}
                # Append the new dictionary to the results list
                results.append(new_dict)
    else:
        # If elem.tag is not 'dict', assume it's iterable
        res_list = []
        for item in elem:
            # Recursively extract key and value using separate temporary lists
            if item.tag == 'dict':
                test_key = helper.get_elements_after_key(item, 'WFKey', 'dict')
                if test_key is None:
                    test_value = helper.get_elements_after_key(item, 'WFValue', 'dict')
                    if test_value is None:
                        item = helper.get_final_value(item)
                        res_list.append(helper.get_attachments_by_range(item))
                        continue
                key_results = []
                value_results = []
                key = recursive_dict(item, 'WFKey', key_results)
                value = recursive_dict(item, 'WFValue', value_results)
                # Create a new dictionary with the key-value pair
                new_dict = {'key': key, 'value': value}
                # Append the new dictionary to the results list
                res_list.append(new_dict)
            elif item.tag == 'array':
                res_list.append(recursive_dict(item, '', flat=True))
            else:
                res_list.append(helper.extract_value(item))

        results.append(res_list)

    temp_result = results
    results = []
    return temp_result

# def recursive_dict(elem, key_or_value, results=None):
#     if results is None:
#         results = []
#
#     elems = helper.get_elements_after_key(elem, key_or_value, 'dict')
#     if elems is None:
#         if len(results) == 0:
#             return ''
#         return results  # Return the accumulated results so far
#
#     elem = helper.get_final_value(elems[0])
#
#     if elem.tag == 'dict':
#         items_array = helper.get_elements_after_key(elem, 'WFDictionaryFieldValueItems', 'array')
#         if not items_array:
#             # No 'WFDictionaryFieldValueItems' key, try to extract value directly
#             return helper.get_attachments_by_range(elem)
#         else:
#             # 'WFDictionaryFieldValueItems' exists, so it's a nested dictionary
#             items = list(items_array[0])
#             for item in items:
#                 # Recursively extract key and value using separate temporary lists
#                 key_results = []
#                 value_results = []
#                 key = recursive_dict(item, 'WFKey', key_results)
#                 value = recursive_dict(item, 'WFValue', value_results)
#                 # Create a new dictionary with the key-value pair
#                 new_dict = {'key': key, 'value': value}
#                 # Append the new dictionary to the results list
#                 results.append(new_dict)
#     else:
#         # If elem.tag is not 'dict', assume it's iterable
#         for item in elem:
#             # Recursively extract key and value using separate temporary lists
#             key_results = []
#             value_results = []
#             key = recursive_dict(item, 'WFKey', key_results)
#             value = recursive_dict(item, 'WFValue', value_results)
#             # Create a new dictionary with the key-value pair
#             new_dict = {'key': key, 'value': value}
#             # Append the new dictionary to the results list
#             results.append(new_dict)
#
#     temp_result = results
#     results = []
#     return temp_result


def action_dictionary(elem):
    """
    Extracts the actions from the WFWorkflowActions array.

    Parameters:
    - elem (Element): The XML element containing the actions.

    Returns:
    - A list of dictionaries representing the actions.
    - E.g., {'data': {'hi': 'Clipboard (attachment)'}, 'uuid': 'B166A8A3-5412-4072-BC4D-F6755E126C2C'}
    """
    ret_actions = []
    if not helper.check_validation(elem):
        return helper.append_data({'Input': ''}, None)
    child = list(elem)
    values = []
    i = 0
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.get_elements_after_key(elem, 'CustomOutputName', 'string')
    if custom_output_name is not None:
        custom_output_name = custom_output_name[0].text

    while i < len(child):
        current_element = child[i]
        if current_element.tag == 'key':
            key_name = current_element.text
            if key_name == 'WFItems':
                i += 1
                values = child[i]
                break
        i += 1
    # In case that there is no 'WFItems' key in the dictionary
    if i == len(child):
        if custom_output_name is not None:
            return helper.append_data({'Input': '', 'Custom Output Name': custom_output_name}, uuid)
        return helper.append_data('', uuid)
    root = helper.get_all_dicts_at_depth_n(values, 1)[0]
    array_of_dic = list(list(root)[1])
    for item in array_of_dic:
        key_value = recursive_dict(item, 'WFKey')
        value_value = recursive_dict(item, 'WFValue')
        # Create a new dictionary with the key-value pair
        new_dict = {'key': key_value, 'value': value_value}
        # Append the new dictionary to the ret_actions list
        ret_actions.append(new_dict)

    if custom_output_name is not None:
        return helper.append_data({'Input': ret_actions, 'Custom Output Name': custom_output_name}, uuid)
    return helper.append_data({'Input': ret_actions}, uuid)

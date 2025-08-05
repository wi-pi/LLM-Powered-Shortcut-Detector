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


def action_downloadurl(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Get contents of': '', 'Method': 'GET', 'Headers': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output name if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the get type input
    get_type = helper.extract_value_from_string_or_dict(elem, 'WFURL')
    if get_type is None:
        get_type = ''

    # Get the from input
    from_input = helper.extract_value_from_string_or_dict(elem, 'WFHTTPMethod')
    if from_input is None:
        from_input = 'GET'

    res = {'Get contents of': get_type, 'Method': from_input}

    # Get the header if GET
    header = helper.get_elements_after_key(elem, 'WFHTTPHeaders', 'dict')
    if header is not None:
        res['Headers'] = recursive_dict(header[0], '', flat=True)
    else:
        res['Headers'] = ''

    # Get the request body if not get
    if from_input != 'GET':
        # Get the request body type
        body_type = helper.extract_value_from_string_or_dict(elem, 'WFHTTPBodyType')
        if body_type is None:
            body_type = 'JSON'
        res['Request Body'] = body_type
        key = ''
        if body_type == 'JSON' or body_type == 'File':
            if body_type == 'File':
                key = 'File'
            body = helper.get_elements_after_key(elem, 'WFJSONValues', 'dict')
            if body is not None:
                res[key] = recursive_dict(body[0], '', flat=True)
            else:
                res[key] = ''
        else:
            body = helper.get_elements_after_key(elem, 'WFFormValues', 'dict')
            if body is not None:
                res[key] = recursive_dict(body[0], '', flat=True)
            else:
                res[key] = ''

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
import parse_xml.parse_shortcut_WF as helper


def action_getvalueforkey(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Get': 'Value', 'for': '', 'in': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.track_custom_name(elem)

    res = {}

    # Get the get -- by default it is 'Value', should be a string after key 'WFGetDictionaryValueType'
    get_prompt = 'Value'
    get_elem = helper.get_elements_after_key(elem, 'WFGetDictionaryValueType', 'string')
    if get_elem is not None:
        get_prompt = get_elem[0].text
    res['Get'] = get_prompt

    # If we are getting 'Value', we will need to ask for the key
    if get_prompt == 'Value':
        key = helper.extract_value_from_string_or_dict(elem, 'WFDictionaryKey')
        if key is None:
            key = ''
        res['for'] = key

    # Get the input of the action -- must be a dict after WFInput
    input_text = ''
    input_text_elem = helper.get_elements_after_key(elem, 'WFInput', 'dict')
    if input_text_elem is not None:
        input_text_elem = helper.get_final_value(input_text_elem[0])
        input_text = helper.get_attachments_by_range(input_text_elem)

    res['in'] = input_text



    if custom_output_name is not None:
        res['Output Name'] = custom_output_name
    return helper.append_data(res, uuid)

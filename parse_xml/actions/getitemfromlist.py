import parse_xml.parse_shortcut_WF as helper

def action_getitemfromlist(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Get Item': 'First Item', 'From':''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    res = {}

    # Find if the element have custom output name
    custom_output_name = helper.track_custom_name(elem)

    # Get what to get, could be "Ask each time (dict)", "Items in Range", "Item at Index", "Random Item", "Last Item", "First Item"
    get_item = helper.extract_value_from_string_or_dict(elem, 'WFItemSpecifier')
    if get_item is None:
        get_item = 'First Item'
    res['Get Item'] = get_item

    # Get the list -- WFInput
    from_list = ''
    from_list_elem = helper.get_elements_after_key(elem, 'WFInput', 'dict')
    if from_list_elem is not None:
        from_list = helper.get_final_value(from_list_elem[0])
        from_list = helper.get_attachments_by_range(from_list)
    res['From'] = from_list

    # For Item at Index range
    if get_item == "Item At Index":
        index = helper.extract_value_from_string_or_dict(elem, 'WFItemIndex')
        if index is None:
            index = '1'
        res['Index'] = index
    elif get_item == 'Items in Range':
        # Get Start and End Index
        start_index = helper.extract_value_from_string_or_dict(elem, 'WFItemRangeStart')
        if start_index is None:
            start_index = ''
        end_index = helper.extract_value_from_string_or_dict(elem, 'WFItemRangeEnd')
        if end_index is None:
            end_index = ''
        res['Start Index'] = start_index
        res['End Index'] = end_index

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)

import parse_xml.parse_shortcut_WF as helper


def action_text_match_getgroup(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Input': '', 'Type': 'Group At Index', 'Index': '1'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.get_elements_after_key(elem, 'CustomOutputName', 'string')
    if custom_output_name is not None:
        custom_output_name = custom_output_name[0].text

    # Get the matches, only dict
    input_text = ''
    input_text_elem = helper.get_elements_after_key(elem, 'matches', 'dict')
    if input_text_elem is not None:
        input_text_elem = helper.get_final_value(input_text_elem[0])
        input_text = helper.get_attachments_by_range(input_text_elem)

    res = {'Input': input_text}

    # Get the type
    group_type = helper.extract_value_from_string_or_dict(elem, 'WFGetGroupType')
    if group_type is None:
        group_type = 'Group At Index'
    res['Type'] = group_type

    # Get the index
    if group_type == 'Group At Index':
        index = helper.extract_value_from_string_or_dict(elem, 'WFGroupIndex')
        if index is None:
            index = '1'
        res['Index'] = index

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
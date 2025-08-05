import parse_xml.parse_shortcut_WF as helper


def action_text_replace(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Input': '', 'Find': '', 'Replace': '', 'Case Sensitive': True, 'Regular Expression': False}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.get_elements_after_key(elem, 'CustomOutputName', 'string')
    if custom_output_name is not None:
        custom_output_name = custom_output_name[0].text

    # Get the input -- string or dict after text
    input_text_elem = helper.extract_value_from_string_or_dict(elem, 'WFInput')
    if input_text_elem is None:
        input_text_elem = ''

    res = {'Input': input_text_elem}

    # Get the find -- array or string or dict after find
    find_text_elem = helper.extract_value_from_string_or_dict(elem, 'WFReplaceTextFind')
    if find_text_elem is None:
        find_text_elem = ''
    res['Find'] = find_text_elem


    # Get the replace -- array or string or dict after replace
    replace_text_elem = helper.extract_value_from_string_or_dict(elem, 'WFReplaceTextReplace')
    if replace_text_elem is None:
        replace_text_elem = ''
    res['Replace'] = replace_text_elem

    # Get the case sensitive
    case_sensitive = helper.get_elements_after_key(elem, 'WFReplaceTextCaseSensitive', 'false')
    if case_sensitive is None:
        case_sensitive = True
    else:
        case_sensitive = False
    res['Case Sensitive'] = case_sensitive

    # Get the regular expression
    regular_expression = helper.get_elements_after_key(elem, 'WFReplaceTextRegularExpression', 'true')
    if regular_expression is None:
        regular_expression = False
    else:
        regular_expression = True
    res['Regular Expression'] = regular_expression

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
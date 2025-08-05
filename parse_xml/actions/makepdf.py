import parse_xml.parse_shortcut_WF as helper


def action_makepdf(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'From': '', 'Include Margin': False, 'Include': 'All Pages', 'Merge Behavior': 'Append'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output name if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the from input
    from_input = helper.extract_value_from_string_or_dict(elem, 'WFInput')
    if from_input is None:
        from_input = ''

    # Get the include margin input
    margin = helper.get_elements_after_key(elem, 'WFPDFIncludeMargin', 'true')
    if margin is not None:
        margin = True
    else:
        margin = False

    # Get the include input
    include_input = helper.extract_value_from_string_or_dict(elem, 'WFPDFIncludedPages')
    if include_input is None:
        include_input = 'All Pages'

    res = {'From': from_input, 'Include Margin': margin, 'Include': include_input}

    if include_input == 'Single Page':
        # Get the page number
        page_number = helper.extract_value_from_string_or_dict(elem, 'WFPDFSinglePage')
        if page_number is None:
            page_number = '1'
        res['Page #'] = page_number
    elif include_input == 'Page Range':
        # Get the page range
        page_range_start = helper.extract_value_from_string_or_dict(elem, 'WFPDFPageRangeStart')
        if page_range_start is None:
            page_range_start = '1'
        page_range_end = helper.extract_value_from_string_or_dict(elem, 'WFPDFPageRangeEnd')
        if page_range_end is None:
            page_range_end = '3'
        res['Start Page #'] = page_range_start
        res['End Page #'] = page_range_end

    # Get the merge behavior input
    merge_behavior = helper.extract_value_from_string_or_dict(elem, 'WFPDFMergeBehavior')
    if merge_behavior is None:
        merge_behavior = 'Append'

    res['Merge Behavior'] = merge_behavior

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
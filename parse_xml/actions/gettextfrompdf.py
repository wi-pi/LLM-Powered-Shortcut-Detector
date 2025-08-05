import parse_xml.parse_shortcut_WF as helper


def action_gettextfrompdf(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Get': '', 'from PDF': '', 'Page Header Text': '', 'Page Footer Text': '', 'Combine Pages': True}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output name if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the get input
    input_elem = helper.extract_value_from_string_or_dict(elem, 'WFGetTextFromPDFTextType')
    if input_elem is None:
        input_elem = 'Text'

    # Get the from input
    from_input = helper.get_elements_after_key(elem, 'WFInput', 'dict')
    if from_input is None:
        from_input = ''
    else:
        from_input = helper.parse_file_input(from_input[0], 'WFInput')

    # Get the page header text
    page_header_text = helper.extract_value_from_string_or_dict(elem, 'WFGetTextFromPDFPageHeader')
    if page_header_text is None:
        page_header_text = ''

    # Get the page footer text
    page_footer_text = helper.extract_value_from_string_or_dict(elem, 'WFGetTextFromPDFPageFooter')
    if page_footer_text is None:
        page_footer_text = ''

    # Get the combine pages input
    combine_page = helper.get_elements_after_key(elem, 'WFCombinePages', 'false')
    if combine_page is not None:
        combine_page = False
    else:
        combine_page = True

    res = {'Get': input_elem, 'from PDF': from_input, 'Page Header Text': page_header_text, 'Page Footer Text': page_footer_text, 'Combine Pages': combine_page}


    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
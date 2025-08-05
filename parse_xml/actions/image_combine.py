import parse_xml.parse_shortcut_WF as helper


def action_image_combine(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Combine': 'Choose', '': 'Horizontally', 'Spacing': '0'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output name if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the get type input
    get_type = ''
    get_type_elem = helper.get_elements_after_key(elem, 'WFInput', 'array')
    if get_type_elem is None:
        get_type = helper.extract_value_from_string_or_dict(elem, 'WFInput')
    else:
        get_type = []
        for item in get_type_elem[0]:
            item = helper.get_final_value(item)
            get_type.append(helper.get_attachments_by_range(item))
        if len(get_type_elem[0]) < 1:
            get_type = 'Choose'

    # Get the mode
    from_input = helper.extract_value_from_string_or_dict(elem, 'WFImageCombineMode')
    if from_input is None:
        from_input = 'Horizontally'

    # Get the spacing
    spacing = helper.extract_value_from_string_or_dict(elem, 'WFImageCombineSpacing')
    if spacing is None:
        spacing = '0'

    res = {'Combine': get_type, '': from_input, 'Spacing': spacing}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
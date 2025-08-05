import parse_xml.parse_shortcut_WF as helper


def action_selectphoto(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Select Photos': '', 'Include': 'All', 'Select Multiple': True}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.track_custom_name(elem)

    # Get the include
    input_text = helper.get_elements_after_key(elem, 'WFPhotoPickerTypes', 'array')
    input_type = ''
    if input_text is not None:
        for i in input_text[0]:
            input_type += i.text + ', '
    if input_text is None:
        input_text = helper.extract_value_from_string_or_dict(elem, 'WFPhotoPickerTypes')
        if input_text is None:
            input_type = 'All'
        else:
            input_type = input_text

    res = {'Select Photos': '', 'Include': input_type}

    # Get the select multiple
    select_multiple = helper.get_elements_after_key(elem, 'WFSelectMultiplePhotos', 'true')
    if select_multiple is not None:
        select_multiple = True
    else:
        select_multiple = False

    res['Select Multiple'] = select_multiple

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
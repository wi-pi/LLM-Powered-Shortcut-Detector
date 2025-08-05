import parse_xml.parse_shortcut_WF as helper

def action_image_removebackground(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Remove Background from': '', 'Crop': False}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.track_custom_name(elem)

    # Get the input
    input_text = helper.extract_value_from_string_or_dict(elem, 'WFInput')
    if input_text is None:
        input_text = ''

    res = {'Remove Background from': input_text}

    # Get the crop
    crop = helper.get_elements_after_key(elem, 'WFCropToBounds', 'true')
    if crop is not None:
        crop = True
    else:
        crop = False

    res['Crop'] = crop

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
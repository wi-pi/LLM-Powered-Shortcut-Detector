import parse_xml.parse_shortcut_WF as helper


def action_takephoto(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Show Preview': True, '# of Photo': '1', 'Camera': 'Back'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.get_elements_after_key(elem, 'CustomOutputName', 'string')
    if custom_output_name is not None:
        custom_output_name = custom_output_name[0].text

    # Get show preview boolean
    show_preview = True
    show_preview_elem = helper.get_elements_after_key(elem, 'WFCameraCaptureShowPreview', 'false')
    if show_preview_elem is not None:
        show_preview = False

    res = {'Show Preview': show_preview}

    # Get the number of photos if show preview is true
    number_of_photo = '1'
    if show_preview:
        number_of_photo_elem = helper.get_elements_after_key(elem, 'WFPhotoCount', 'real')
        if number_of_photo_elem is not None:
            number_of_photo = number_of_photo_elem[0].text
    res['# of Photo'] = number_of_photo

    # Get the camera
    camera = 'Back'
    camera_elem = helper.extract_value_from_string_or_dict(elem, 'WFCameraCaptureDevice')
    if camera_elem is not None:
        camera = camera_elem
    res['Camera'] = camera

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
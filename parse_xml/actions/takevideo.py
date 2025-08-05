import parse_xml.parse_shortcut_WF as helper


def action_takevideo(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Camera': 'Back', 'Quality': 'High', 'Start Recording': 'Immediately'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.get_elements_after_key(elem, 'CustomOutputName', 'string')
    if custom_output_name is not None:
        custom_output_name = custom_output_name[0].text

    # Get the camera
    camera = 'Back'
    camera_elem = helper.extract_value_from_string_or_dict(elem, 'WFCameraCaptureDevice')
    if camera_elem is not None:
        camera = camera_elem
    res = {'Camera': camera}

    # Get the video quality
    video_quality = 'High'
    video_quality_elem = helper.extract_value_from_string_or_dict(elem, 'WFCameraCaptureQuality')
    if video_quality_elem is not None:
        video_quality = video_quality_elem
    res['Quality'] = video_quality

    # Get the start recording time
    start_recording_time = 'Immediately'
    start_recording_time_elem = helper.extract_value_from_string_or_dict(elem, 'WFStartRecording')
    if start_recording_time_elem is not None:
        start_recording_time = start_recording_time_elem
    res['Start Recording'] = start_recording_time

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
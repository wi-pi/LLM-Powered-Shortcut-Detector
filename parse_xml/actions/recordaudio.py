import parse_xml.parse_shortcut_WF as helper


def action_recordaudio(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Audio Quality': 'Normal', 'Start Recording': 'On Tap', 'Finish Recording': 'On Tap'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.get_elements_after_key(elem, 'CustomOutputName', 'string')
    if custom_output_name is not None:
        custom_output_name = custom_output_name[0].text

    # Get the audio quality
    audio_quality = 'Normal'
    audio_quality_elem = helper.extract_value_from_string_or_dict(elem, 'WFRecordingCompression')
    if audio_quality_elem is not None:
        audio_quality = audio_quality_elem
    res = {'Audio Quality': audio_quality}

    # Get the start recording time
    start_recording_time = 'On Tap'
    start_recording_time_elem = helper.extract_value_from_string_or_dict(elem, 'WFRecordingStart')
    if start_recording_time_elem is not None:
        start_recording_time = start_recording_time_elem
    res['Start Recording'] = start_recording_time

    # Get the finish recording time
    finish_recording_time = 'On Tap'
    finish_recording_time_elem = helper.extract_value_from_string_or_dict(elem, 'WFRecordingEnd')
    if finish_recording_time_elem is not None:
        finish_recording_time = finish_recording_time_elem
    res['Finish Recording'] = finish_recording_time

    # Get the Duration if Finish Recording is 'After Time'
    if finish_recording_time == 'After Time':
        duration_mag = '0'
        duration_unit = 'minutes'
        duration_elem = helper.get_elements_after_key(elem, 'WFRecordingTimeInterval', 'dict')
        if duration_elem is not None:
            duration_elem = helper.get_final_value(duration_elem[0])
            duration_mag = helper.extract_value_from_string_or_dict(duration_elem, 'Magnitude')
            if duration_mag is None:
                duration_mag = '0'
            duration_unit = helper.extract_value_from_string_or_dict(duration_elem, 'Unit')
            if duration_unit is None:
                duration_unit = 'minutes'
        res['Duration Magnitude'] = duration_mag
        res['Duration Unit'] = duration_unit

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
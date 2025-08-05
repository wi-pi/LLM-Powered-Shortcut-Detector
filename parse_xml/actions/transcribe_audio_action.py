import parse_xml.parse_shortcut_WF as helper


def action_transcribe_audio(elem):
    if not helper.check_validation(elem):
        raise ValueError('Invalid transcribe audio action')

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.get_elements_after_key(elem, 'CustomOutputName', 'string')
    if custom_output_name is not None:
        custom_output_name = custom_output_name[0].text

    # Get the input of the action -- must be a dict of file
    input_text = ''
    input_text_elem = helper.get_elements_after_key(elem, 'audioFile', 'dict')
    if input_text_elem is not None:
        input_text = helper.unpack_file_dict(input_text_elem[0])

    res = {'Transcribe to Text': input_text}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
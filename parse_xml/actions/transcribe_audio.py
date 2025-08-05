import parse_xml.parse_shortcut_WF as helper


def action_transcribe_audio(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Transcribe': ''}, None)


    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output name if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the transcribe input
    parse_elem = helper.extract_value_from_string_or_dict(elem, 'audioFile')
    if parse_elem is None:
        parse_elem = ''

    res = {'Transcribe': parse_elem}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
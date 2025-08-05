import parse_xml.parse_shortcut_WF as helper

def action_makespokenaudiofromtext(elem):
    if not helper.check_validation(elem):
        raise ValueError('Invalid element make spoken audio from text')

    # Check UUID
    uuid = helper.track_uuid(elem)

    res = {}

    # Find if the element have custom output name
    custom_output_name = helper.get_elements_after_key(elem, 'CustomOutputName', 'string')
    if custom_output_name is not None:
        custom_output_name = custom_output_name[0].text

    # Get the input
    text_elem = helper.extract_value_from_string_or_dict(elem, 'WFInput')
    if text_elem is None:
        text_elem = ''


    # Get the rate
    rate_elem = helper.get_elements_after_key(elem, 'WFSpeakTextRate', 'real')
    if rate_elem is not None:
        rate_elem = rate_elem[0].text
    else:
        rate_elem = 0.5

    # Get the pitch
    pitch_elem = helper.get_elements_after_key(elem, 'WFSpeakTextPitch', 'real')
    if pitch_elem is not None:
        pitch_elem = pitch_elem[0].text
    else:
        pitch_elem = 1

    res = {'Input': text_elem, 'Rate': rate_elem, 'Pitch': pitch_elem}

    # Get the language
    language = 'en-US'
    language_elem = helper.get_elements_after_key(elem, 'WFSpeakTextLanguage', 'string')
    if language_elem is not None:
        language = language_elem[0].text
        res['Language'] = language
    else:
        language_elem = helper.get_elements_after_key(elem, 'WFSpeakTextLanguage', 'dict')
        if language_elem is not None:
            language = helper.get_final_value(language_elem[0])
            language = helper.get_attachments_by_range(language)
        res['Language'] = language
        # Get voice
        voice = helper.extract_value_from_string_or_dict(elem, 'WFSpeakTextVoice')
        if voice is None:
            voice = 'com.apple.eloquence.en-US.Samantha'
        res['Voice'] = voice

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
import parse_xml.parse_shortcut_WF as helper


def action_speaktext(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Input': '', 'Wait Until Finished': True, 'Rate': 0.5, 'Pitch': 1, 'Language': 'en-US', 'Voice': 'com.apple.eloquence.en-US.Samantha'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom name
    custom_name = helper.track_custom_name(elem)

    # Get the text
    text_elem = helper.extract_value_from_string_or_dict(elem, 'WFText')
    if text_elem is None:
        text_elem = ''
    else:
        if len(text_elem) == 0:
            text_elem = ''

    # Get wait until finished
    wait_elem = helper.get_elements_after_key(elem, 'WFSpeakTextWait', 'false')
    if wait_elem is not None:
        wait_elem = False
    else:
        wait_elem = True

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

    res = {'Input': text_elem, 'Wait Until Finished': wait_elem, 'Rate': rate_elem, 'Pitch': pitch_elem}

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

    if custom_name is not None:
        res['Output Name'] = custom_name

    return helper.append_data(res, uuid)
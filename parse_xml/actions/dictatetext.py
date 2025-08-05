import parse_xml.parse_shortcut_WF as helper


def action_dictatetext(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Language': 'English (United States)', 'Stop Listening': 'After Pause'}, None)
        # raise ValueError('Invalid Dictate Text action')

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.track_custom_name(elem)

    # Get the language
    language = helper.extract_value_from_string_or_dict(elem, 'WFSpeechLanguage')
    if language is None:
        language = 'English (United States)'

    # Get stop listening
    stop_listening = helper.extract_value_from_string_or_dict(elem, 'WFDictateTextStopListening')
    if stop_listening is None:
        stop_listening = 'After Pause'

    res = {'Language': language, 'Stop Listening': stop_listening}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
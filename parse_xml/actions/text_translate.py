import parse_xml.parse_shortcut_WF as helper


def action_text_translate(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Input': '', 'Language': 'Detected Language', 'Target Language': 'en-US'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.track_custom_name(elem)

    # Get the input of the action -- must be a dict or a string
    input_text_elem = helper.extract_value_from_string_or_dict(elem, 'WFInputText')
    if input_text_elem is None:
        input_text_elem = ''
    res = {'Input': input_text_elem}

    # Get the input langauge, default is detected language
    language_input = helper.extract_value_from_string_or_dict(elem, 'WFSelectedFromLanguage')
    if language_input is None:
        language_input = 'Detected Language'
    res['Language'] = language_input

    # Get the target language
    target_language = helper.extract_value_from_string_or_dict(elem, 'WFSelectedLanguage')
    if target_language is None:
        target_language = 'en-US'
    res['Target Language'] = target_language

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name
    return helper.append_data(res, uuid)

import parse_xml.parse_shortcut_WF as helper


def action_ask(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Ask for': '', 'with': '', 'Default Answer': '', 'Allow Multiple Lines': True}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.track_custom_name(elem)

    # Get the prompt.txt of the question, it could be either a string or a dict
    prompt_elem = helper.extract_value_from_string_or_dict(elem, 'WFAskActionPrompt')
    if prompt_elem is None:
        prompt_elem = ''


    # Check the type of question
    question_type = 'Text'
    question_type_elem = helper.get_elements_after_key(elem, 'WFInputType', 'string')

    if question_type_elem is not None:
        question_type = question_type_elem[0].text

    res_dict = {
        'Ask for': question_type,
        'with': prompt_elem,
    }

    if question_type == 'Text':
        # Get Default Answer, if have
        default_answer = ''
        default_answer = helper.get_elements_after_key(elem, 'WFAskActionDefaultAnswer', 'string')
        if default_answer is not None:
            default_answer = default_answer[0].text
        else:
            # Try dictionary
            default_answer = helper.get_elements_after_key(elem, 'WFAskActionDefaultAnswer', 'dict')
            if default_answer is not None:
                default_answer = helper.get_final_value(default_answer[0])
                default_answer = helper.get_attachments_by_range(default_answer)
            else:
                default_answer = ''

        # Find it is allows multiple lines
        allow_multiple_lines = True
        allow_multiple_lines_elem = helper.get_elements_after_key(elem, 'WFAllowsMultilineText', 'false')
        if allow_multiple_lines_elem is not None:
            allow_multiple_lines = False

        res_dict['Default Answer'] = default_answer
        res_dict['Allow Multiple Lines'] = allow_multiple_lines

    elif question_type == 'Date and Time':
        # Get the default Date and Time
        default_date_time = ''
        default_date_time_elem = helper.get_elements_after_key(elem, 'WFAskActionDefaultAnswerDateAndTime', 'string')
        # If it is a string
        if default_date_time_elem is not None:
            default_date_time = default_date_time_elem[0].text
        else:
            # Try dictionary
            default_date_time_elem = helper.get_elements_after_key(elem, 'WFAskActionDefaultAnswerDateAndTime', 'dict')
            if default_date_time_elem is not None:
                default_date_time = helper.get_final_value(default_date_time_elem[0])
                default_date_time = helper.get_attachments_by_range(default_date_time)
            else:
                default_date_time = ''

        # Get the date style
        res_dict['Default Date and Time'] = default_date_time

    elif question_type == 'Number':
        # Get if allow decimal number
        allow_decimal_number = True
        allow_decimal_number_elem = helper.get_elements_after_key(elem, 'WFAskActionAllowsDecimalNumbers', 'false')
        if allow_decimal_number_elem is not None:
            allow_decimal_number = False

        # Get allow negative number
        allow_negative_number = True
        allow_negative_number_elem = helper.get_elements_after_key(elem, 'WFAskActionAllowsNegativeNumbers', 'false')
        if allow_negative_number_elem is not None:
            allow_negative_number = False

        # Get the default number -- either a string or a dict
        default_number = ''
        default_number_elem = helper.get_elements_after_key(elem, 'WFAskActionDefaultAnswerNumber', 'string')
        if default_number_elem is not None:
            default_number = default_number_elem[0].text
        else:
            default_number_elem = helper.get_elements_after_key(elem, 'WFAskActionDefaultAnswerNumber', 'dict')
            if default_number_elem is not None:
                default_number = helper.get_final_value(default_number_elem[0])
                default_number = helper.get_attachments_by_range(default_number)
            else:
                default_number = ''

        res_dict['Allow Decimal Numbers'] = allow_decimal_number
        res_dict['Allow Negative Numbers'] = allow_negative_number
        res_dict['Default Number'] = default_number

    elif question_type == 'Time':
        # Get the default time
        default_time = ''
        default_time_elem = helper.get_elements_after_key(elem, 'WFAskActionDefaultAnswerTime', 'string')
        if default_time_elem is not None:
            default_time = default_time_elem[0].text
        else:
            default_time_elem = helper.get_elements_after_key(elem, 'WFAskActionDefaultAnswerTime', 'dict')
            if default_time_elem is not None:
                default_time = helper.get_final_value(default_time_elem[0])
                default_time = helper.get_attachments_by_range(default_time)
            else:
                default_time = ''

        res_dict['Default Time'] = default_time

    elif question_type == 'Date':
        # Get the default date
        default_date = ''
        default_date_elem = helper.get_elements_after_key(elem, 'WFAskActionDefaultAnswerDate', 'string')
        if default_date_elem is not None:
            default_date = default_date_elem[0].text
        else:
            default_date_elem = helper.get_elements_after_key(elem, 'WFAskActionDefaultAnswerDate', 'dict')
            if default_date_elem is not None:
                default_date = helper.get_final_value(default_date_elem[0])
                default_date = helper.get_attachments_by_range(default_date)
            else:
                default_date = ''

        res_dict['Default Date'] = default_date

    elif question_type == 'URL':
        # Get the default URL
        default_url = ''
        default_url_elem = helper.get_elements_after_key(elem, 'WFAskActionDefaultAnswerURL', 'string')
        if default_url_elem is not None:
            default_url = default_url_elem[0].text
        else:
            default_url_elem = helper.get_elements_after_key(elem, 'WFAskActionDefaultAnswerURL', 'dict')
            if default_url_elem is not None:
                default_url = helper.get_final_value(default_url_elem[0])
                default_url = helper.get_attachments_by_range(default_url)
            else:
                default_url = ''

        res_dict['Default URL'] = default_url
    else:
        raise ValueError(f"Unknown question type: {question_type}")

    if custom_output_name is not None:
        res_dict['Custom Output Name'] = custom_output_name
    return helper.append_data(res_dict, uuid)

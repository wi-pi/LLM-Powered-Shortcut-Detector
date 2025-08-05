import parse_xml.parse_shortcut_WF as helper


def action_open_mailbox(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Open': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output name if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the email input
    email_input = helper.get_elements_after_key(elem, 'target', 'dict')
    if email_input is not None:
        # find the title - key
        cur_elem = helper.get_elements_after_key(email_input[0], 'title', 'dict')
        if cur_elem is not None:
            email_input = helper.extract_value_from_string_or_dict(cur_elem[0], 'key')
        else:
            email_input = helper.extract_value_from_string_or_dict(elem, 'target')
    else:
        email_input = ''

    res = {'Open': email_input}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
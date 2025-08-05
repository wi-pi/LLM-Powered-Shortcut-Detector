import parse_xml.parse_shortcut_WF as helper


def action_sendemail(elem, client_number):
    if not helper.check_validation(elem):
        return helper.append_data({'Send': '', 'to': '', 'as': '', 'Show Compose Sheet': True, 'From': '', 'Cc':'', 'Bcc':''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output name if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the message input
    message_input = helper.extract_value_from_string_or_dict(elem, 'WFSendEmailActionInputAttachments')
    if message_input is None:
        message_input = ''

    # Get the recepient input
    recepient_input = helper.get_elements_after_key(elem, 'WFSendEmailActionToRecipients', 'dict')
    if recepient_input is None:
        recepient_input = []
    else:
        recepient_input = helper.parse_contact_info(recepient_input[0], client_number)

    # Get the cc input
    cc_input = helper.get_elements_after_key(elem, 'WFSendEmailActionCcRecipients', 'dict')
    if cc_input is None:
        cc_input = []
    else:
        cc_input = helper.parse_contact_info(cc_input[0], client_number)

    # Get the bcc input
    bcc_input = helper.get_elements_after_key(elem, 'WFSendEmailActionBccRecipients', 'dict')
    if bcc_input is None:
        bcc_input = []
    else:
        bcc_input = helper.parse_contact_info(bcc_input[0], client_number)

    # Get the subject input
    subject_input = helper.extract_value_from_string_or_dict(elem, 'WFSendEmailActionSubject')
    if subject_input is None:
        subject_input = ''

    # Get the Show Compose Sheet input
    show_compose_sheet_input = helper.get_elements_after_key(elem, 'WFSendEmailActionShowComposeSheet', 'false')
    if show_compose_sheet_input is None:
        show_compose_sheet_input = True
    else:
        show_compose_sheet_input = False

    # Get the from input
    from_input = ''
    if show_compose_sheet_input:
        from_input = helper.extract_value_from_string_or_dict(elem, 'WFSendEmailActionFrom')
    else:
        from_input = helper.extract_value_from_string_or_dict(elem, 'WFEmailAccountActionSelectedAccount')
    if from_input is None:
        from_input = ''

    res = {'Send': message_input, 'to': recepient_input, 'as': subject_input, 'Show Compose Sheet': show_compose_sheet_input, 'From': from_input, 'Cc': cc_input, 'Bcc': bcc_input}

    # get the save draft is not show compose sheet
    if not show_compose_sheet_input:
        save_draft = helper.get_elements_after_key(elem, 'WFSendEmailActionSaveAsDraft', 'true')
        if save_draft is None:
            save_draft = False
        else:
            save_draft = True
        res['Save Draft'] = save_draft

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)

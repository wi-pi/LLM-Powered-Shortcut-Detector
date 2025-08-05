import parse_xml.parse_shortcut_WF as helper


def action_add_new_contact(elem, client_number):
    if not helper.check_validation(elem):
        return helper.append_data({'First Name': '', 'Last Name':'', 'Company': '', 'Photo': '', 'Phone Number': '', 'Email Address': '', 'Notes': '', 'Show Compose Sheet': True}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the contact name
    first_name = helper.extract_value_from_string_or_dict(elem, 'WFContactFirstName')
    if first_name is None:
        first_name = ''

    last_name = helper.extract_value_from_string_or_dict(elem, 'WFContactLastName')
    if last_name is None:
        last_name = ''

    company = helper.extract_value_from_string_or_dict(elem, 'WFContactCompany')
    if company is None:
        company = ''

    photo = helper.extract_value_from_string_or_dict(elem, 'WFContactPhoto')
    if photo is None:
        photo = ''

    contact_elem = helper.get_elements_after_key(elem, 'WFContactPhoneNumbers', 'dict')
    if contact_elem is not None:
        contact_elem = helper.parse_contact_info(contact_elem, client_number)
        if contact_elem == 1:
            contact_elem = helper.extract_value_from_string_or_dict(elem, 'WFContactPhoneNumbers')
    else:
        contact_elem = ''

    email_elem = helper.get_elements_after_key(elem, 'WFContactEmailAddresses', 'dict')
    if email_elem is not None:
        email_elem = helper.parse_contact_info(email_elem, client_number)
    else:
        email_elem = ''

    notes = helper.extract_value_from_string_or_dict(elem, 'WFContactNotes')
    if notes is None:
        notes = ''

    show_compose_sheet = helper.get_elements_after_key(elem, 'ShowWhenRun', 'false')
    if show_compose_sheet is not None:
        show_compose_sheet = False
    else:
        show_compose_sheet = True

    res = {'First Name': first_name, 'Last Name': last_name, 'Company': company, 'Photo': photo, 'Phone Number': contact_elem, 'Email Address': email_elem, 'Notes': notes, 'Show Compose Sheet': show_compose_sheet}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name
    return helper.append_data(res, uuid)
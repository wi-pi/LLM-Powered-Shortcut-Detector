import parse_xml.parse_shortcut_WF as helper


def action_email(elem, client_number):
    if not helper.check_validation(elem):
        return helper.append_data({'Email Address': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output name if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the email input may be array dict or string, find array first
    people_to_call_elem = helper.get_elements_after_key(elem, 'WFEmailAddress', 'dict')
    if people_to_call_elem is not None:
        people_to_call_elem = helper.parse_contact_info(people_to_call_elem[0], client_number)
    else:
        people_to_call_elem = ''

    res = {'Email Address': people_to_call_elem}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
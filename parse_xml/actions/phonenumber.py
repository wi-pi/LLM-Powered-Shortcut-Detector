import parse_xml.parse_shortcut_WF as helper


def action_phonenumber(elem, client_number):
    if not helper.check_validation(elem):
        return helper.append_data({'Phone number': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    number = helper.get_elements_after_key(elem, 'WFPhoneNumber', 'dict')
    if number is None:
        number = ''
    else:
        number = helper.parse_contact_info(number[0], client_number)

    res = {'Phone number': number}


    if custom_output_name is not None:
        res['Output Name'] = custom_output_name
    return helper.append_data(res, uuid)
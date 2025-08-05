import parse_xml.parse_shortcut_WF as helper


def action_contacts(elem, client_number):
    if not helper.check_validation(elem):
        return helper.append_data({'Input': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    recepient_input = helper.get_elements_after_key(elem, 'WFContact', 'dict')
    if recepient_input is None:
        recepient_input = []
    else:
        recepient_input = helper.parse_contact_info(recepient_input[0], client_number)

    res = {'Input': recepient_input}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name
    return helper.append_data(res, uuid)
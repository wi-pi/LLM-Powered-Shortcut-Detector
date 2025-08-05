import parse_xml.parse_shortcut_WF as helper


def action_whatsapp_send(elem, client_number):
    if not helper.check_validation(elem):
        return helper.append_data({'Send Message via WhatsApp': []}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    output_name = helper.track_custom_name(elem)

    recepient_input = helper.get_elements_after_key(elem, 'WhatsAppContact', 'dict')
    if recepient_input is None:
        recepient_input = []
    else:
        recepient_input = helper.parse_contact_info(recepient_input[0], client_number)

    res = {'Send Message via WhatsApp': recepient_input}

    if output_name is not None:
        res['Output Name'] = output_name

    return helper.append_data(res, uuid)
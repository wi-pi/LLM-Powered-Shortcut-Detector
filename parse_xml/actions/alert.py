import parse_xml.parse_shortcut_WF as helper

def action_alert(elem):
    show_cancel_button = True
    if elem.tag == 'dict' and len(elem) == 0:
        res = {'Title': '', 'Message': 'Do you want to continue?', 'Show Cancel Button': show_cancel_button}
        return helper.append_data(res, None)
    # Check UUID
    uuid = helper.track_uuid(elem)

    # Check the cancel button
    cancel_button = helper.get_elements_after_key(elem, 'WFAlertActionCancelButtonShown', 'false')
    if cancel_button is not None:
        show_cancel_button = False

    # Get the title (string or dict)
    title = helper.get_elements_after_key(elem, 'WFAlertActionTitle', 'string')
    if title is None:
        # Try dict
        title = helper.get_elements_after_key(elem, 'WFAlertActionTitle', 'dict')
        if title is None:
            title = ''
        else:
            title = helper.get_final_value(title[0])
            title = helper.get_attachments_by_range(title)
    else:
        title = title[0].text
        if title is None:
            title = ''

    # Get the alert message (string or dict)
    message = helper.get_elements_after_key(elem, 'WFAlertActionMessage', 'string')
    if message is None:
        # Try dict
        message = helper.get_elements_after_key(elem, 'WFAlertActionMessage', 'dict')
        if message is None:
            message = ''
        else:
            message = helper.get_final_value(message[0])
            message = helper.get_attachments_by_range(message)
    else:
        message = message[0].text
        if message is None:
            message = ''

    res = {'Title': title, 'Message': message, 'Show Cancel Button': show_cancel_button}
    return helper.append_data(res, uuid)
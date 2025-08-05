import parse_xml.parse_shortcut_WF as helper


def action_notification(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Body': 'Hello World', 'Title': '', 'Play Sound': True, 'Attachment': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.get_elements_after_key(elem, 'CustomOutputName', 'string')
    if custom_output_name is not None:
        custom_output_name = custom_output_name[0].text

    # Get the body
    body = 'Hello World'
    body_elem = helper.extract_value_from_string_or_dict(elem, 'WFNotificationActionBody')
    if body_elem is not None:
        body = body_elem
    else:
        if helper.fine_key_from_dict(elem, 'WFNotificationActionBody'):
            body = ''
    res = {'Body': body}

    # Get the title
    title = ''
    title_elem = helper.extract_value_from_string_or_dict(elem, 'WFNotificationActionTitle')
    if title_elem is not None:
        title = title_elem

    res['Title'] = title

    # Get the sound
    sound = True
    sound_elem = helper.get_elements_after_key(elem, 'WFNotificationActionSound', 'false')
    if sound_elem is not None:
        sound = False

    res['Play Sound'] = sound

    # Get the attachment
    attachment = ''
    attachment_elem = helper.extract_value_from_string_or_dict(elem, 'WFInput')
    if attachment_elem is not None:
        icon = attachment_elem

    res['Attachment'] = attachment

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
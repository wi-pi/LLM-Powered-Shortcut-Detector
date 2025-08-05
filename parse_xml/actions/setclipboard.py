import parse_xml.parse_shortcut_WF as helper


def action_setclipboard(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Input': '', 'Local Only': False, 'Expire At': 'Today at 3 PM'}, '')

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.get_elements_after_key(elem, 'CustomOutputName', 'string')
    if custom_output_name is not None:
        custom_output_name = custom_output_name[0].text

    # Get the clipboard text input
    clipboard_text = ''
    clipboard_text_elem = helper.get_elements_after_key(elem, 'WFInput', 'dict')
    if clipboard_text_elem is not None:
        clipboard_text_elem = helper.get_final_value(clipboard_text_elem[0])
        clipboard_text = helper.get_attachments_by_range(clipboard_text_elem)

    res = {'Input': clipboard_text}

    # Get if it is Local Only
    local_only = False
    local_only_elem = helper.get_elements_after_key(elem, 'WFLocalOnly', 'true')
    if local_only_elem is not None:
        local_only = True
    res['Local Only'] = local_only

    # Get Expire time
    expire_time = 'Today at 3 PM'
    expire_time_elem = helper.extract_value_from_string_or_dict(elem, 'WFExpirationDate')
    if expire_time_elem is not None:
        expire_time = expire_time_elem
    res['Expire At'] = expire_time

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
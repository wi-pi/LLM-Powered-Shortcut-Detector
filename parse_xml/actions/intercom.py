import parse_xml.parse_shortcut_WF as helper


def action_intercom(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Intercom': '', 'to': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output name if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the intercom input may be array dict or string, find array first
    inter_res = []
    intercom_input = helper.get_elements_after_key(elem, 'WFInput', 'array')
    if intercom_input is not None:
        for item in intercom_input[0]:
            current_elem = helper.get_final_value(item)
            inter_res.append(helper.get_attachments_by_range(current_elem))
    else:
        inter_res = helper.extract_value_from_string_or_dict(elem, 'WFInput')
        if inter_res is None:
            inter_res = ''

    # Get the home
    home = helper.extract_value_from_string_or_dict(elem, 'WFHome')

    res = {'Intercom': inter_res, 'to': home}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
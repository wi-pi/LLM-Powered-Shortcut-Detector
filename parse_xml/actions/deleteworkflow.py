import parse_xml.parse_shortcut_WF as helper


def action_deleteworkflow(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Delete': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    shortcut = []
    res_elem = helper.get_elements_after_key(elem, 'entities', 'array')
    if res_elem is not None:
        for item in res_elem[0]:
            item = helper.get_elements_after_key(item, 'title', 'dict')
            shortcut.append(helper.extract_value_from_string_or_dict(item[0], 'key'))
    else:
        shortcut = helper.get_elements_after_key(elem, 'entities', 'dict')
        if shortcut is not None:
            shortcut = helper.get_elements_after_key(shortcut[0], 'title', 'dict')
            if shortcut is not None:
                shortcut = helper.extract_value_from_string_or_dict(shortcut[0], 'key')
            else:
                shortcut = helper.extract_value_from_string_or_dict(elem, 'entities')
    if shortcut is None:
        shortcut = ''

    res = {'Delete': shortcut}


    if custom_output_name is not None:
        res['Output Name'] = custom_output_name
    return helper.append_data(res, uuid)
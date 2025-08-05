import parse_xml.parse_shortcut_WF as helper


def action_setting_opens(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Open': 'Sounds & Haptics'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the type
    type = helper.get_elements_after_key(elem, 'target', 'dict')
    if type is not None:
        type = helper.get_elements_after_key(type[0], 'title', 'dict')
        if type is not None:
            type = helper.extract_value_from_string_or_dict(type[0], 'key')
        else:
            type = helper.extract_value_from_string_or_dict(elem, 'target')
    else:
        type = 'Sounds & Haptics'

    res = {'Open': type}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
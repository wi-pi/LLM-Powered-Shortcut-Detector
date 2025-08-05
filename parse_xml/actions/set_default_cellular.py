import parse_xml.parse_shortcut_WF as helper


def action_set_default_cellular(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Set Default Line to': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    to = helper.extract_value_from_string_or_dict(elem, 'plan')
    if to is None:
        to = ''

    res =  {'Set Default Line to': to}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name
    return helper.append_data(res, uuid)
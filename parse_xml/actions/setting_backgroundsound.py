import parse_xml.parse_shortcut_WF as helper


def action_setting_backgroundsound(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Change background sound to': 'Balanced Noise'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the type
    type = helper.extract_value_from_string_or_dict(elem, 'backgroundSound')
    if type is None:
        type = 'Balanced Noise'

    res = {'Change background sound to': type}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
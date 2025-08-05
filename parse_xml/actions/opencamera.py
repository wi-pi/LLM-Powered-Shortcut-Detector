import parse_xml.parse_shortcut_WF as helper


def action_open_camera(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Open mode': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    mode = helper.get_elements_after_key(elem, 'cameraMode', 'dict')
    if mode is not None:
        mode = helper.extract_value_from_string_or_dict(mode[0], 'identifier')
        if mode is None:
            mode = helper.extract_value_from_string_or_dict(elem, 'cameraMode')
    if mode is None:
        mode = ''

    res = {'Open mode': mode}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name
    return helper.append_data(res, uuid)
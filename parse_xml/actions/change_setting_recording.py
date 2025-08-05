import parse_xml.parse_shortcut_WF as helper


def action_change_setting_recording(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Enable': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # Get operation
    operation = helper.extract_value_from_string_or_dict(elem, 'changeOperation')
    if operation is None:
        operation = 'Enable'
    else:
        operation = helper.list_to_str(operation)

    # Get change
    change = helper.extract_value_from_string_or_dict(elem, 'setting')
    if change is None:
        change = ''

    res = {operation: change}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name
    return helper.append_data(res, uuid)
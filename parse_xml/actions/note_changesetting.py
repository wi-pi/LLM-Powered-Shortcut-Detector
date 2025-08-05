import parse_xml.parse_shortcut_WF as helper


def action_note_changesetting(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Enable': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the setting action
    operation = helper.extract_value_from_string_or_dict(elem, 'changeOperation')
    if operation is None:
        operation = 'Enable'
    operation = helper.list_to_str(operation)

    # Get the setting
    setting = helper.extract_value_from_string_or_dict(elem, 'setting')
    if setting is None:
        setting = ''

    res = {operation: setting}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name
    return helper.append_data(res, uuid)
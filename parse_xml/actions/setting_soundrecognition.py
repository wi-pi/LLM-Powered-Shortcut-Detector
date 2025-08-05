import parse_xml.parse_shortcut_WF as helper


def action_setting_soundrecognition(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Activate': 'Sound Recognition'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    output_name = helper.track_custom_name(elem)

    action = helper.extract_value_from_string_or_dict(elem, 'operation')
    if action is None:
        action = 'Activate'
    else:
        action = helper.list_to_str(action)

    res = {action: 'Sound Recognition'}

    if output_name is not None:
        res['Output Name'] = output_name

    return helper.append_data(res, uuid)
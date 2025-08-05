import parse_xml.parse_shortcut_WF as helper


def action_setting_magnifier(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Action': 'Open Magnifier'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    res = {'Action': 'Open Magnifier'}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
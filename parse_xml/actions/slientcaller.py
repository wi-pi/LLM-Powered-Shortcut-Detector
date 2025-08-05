import parse_xml.parse_shortcut_WF as helper


def action_slientcaller(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Action': 'Silent Unknown Caller'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output name if have
    custom_output_name = helper.track_custom_name(elem)

    res = {'Action': 'Silent Unknown Caller'}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
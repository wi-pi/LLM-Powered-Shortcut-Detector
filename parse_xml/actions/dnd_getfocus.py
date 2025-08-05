import parse_xml.parse_shortcut_WF as helper


def action_dnd_getfocus(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Action': 'Get Current Focus'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.track_custom_name(elem)

    res = {'Action': 'Get Current Focus'}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
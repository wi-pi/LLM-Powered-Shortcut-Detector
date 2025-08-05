import parse_xml.parse_shortcut_WF as helper


def action_create_newtab(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Action': 'Create New Tab'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.track_custom_name(elem)

    res = {'Action': 'Create New Tab'}
    if custom_output_name is not None:
        res['Output Name'] = custom_output_name
    return helper.append_data(res, uuid)
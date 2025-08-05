import parse_xml.parse_shortcut_WF as helper


def action_getorientation(elem):
    if not helper.check_validation(elem):
        raise ValueError('Invalid get orientation action')

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.get_elements_after_key(elem, 'CustomOutputName', 'string')
    if custom_output_name is not None:
        custom_output_name = custom_output_name[0].text

    res = {'Action': 'Get Orientation'}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
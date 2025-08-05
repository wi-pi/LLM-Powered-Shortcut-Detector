import parse_xml.parse_shortcut_WF as helper


def action_getonscreencontent(elem):
    if not helper.check_validation(elem):
        raise ValueError('Invalid Get On-Screen Content action.')

    # Track the UUID
    uuid = helper.track_uuid(elem)

    # Find if the element has custom output name
    custom_output_name = helper.track_custom_name(elem)

    res = {'Text': 'Get what\'s on screen'}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)


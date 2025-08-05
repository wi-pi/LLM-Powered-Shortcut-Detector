import parse_xml.parse_shortcut_WF as helper


def action_getnameofemoji(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Get name of emoji in': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.track_custom_name(elem)

    # Get the name of emoji
    name_of_emoji = helper.extract_value_from_string_or_dict(elem, 'WFInput')
    if name_of_emoji is None:
        name_of_emoji = ''

    res = {'Get name of emoji in': name_of_emoji}
    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
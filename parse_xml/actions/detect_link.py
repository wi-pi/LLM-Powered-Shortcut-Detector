import parse_xml.parse_shortcut_WF as helper


def action_detect_link(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Get URLs from': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output name if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the link in input
    link_in = helper.extract_value_from_string_or_dict(elem, 'WFInput')
    if link_in is None:
        link_in = ''

    res = {'Get URLs from': link_in}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
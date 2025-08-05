import parse_xml.parse_shortcut_WF as helper


def action_share(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Share': ''}, helper.track_uuid(elem))

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output name if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the item to share
    input = helper.extract_value_from_string_or_dict(elem, 'WFInput')
    if input is None:
        input = ''

    res = {'Share': input}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name
    return helper.append_data(res, uuid)
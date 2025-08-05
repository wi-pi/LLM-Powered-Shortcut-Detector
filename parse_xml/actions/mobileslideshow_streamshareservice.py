import parse_xml.parse_shortcut_WF as helper


def action_mobileslideshow_streamshareservice(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Post': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.track_custom_name(elem)

    # Get the service
    service = helper.extract_value_from_string_or_dict(elem, 'ImageInput')
    if service is None:
        service = ''
    res = {'Post': service}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name
    return helper.append_data(res, uuid)
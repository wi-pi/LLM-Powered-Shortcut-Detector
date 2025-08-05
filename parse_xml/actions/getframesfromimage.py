import parse_xml.parse_shortcut_WF as helper


def action_getframesfromimage(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Get Frames from': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.track_custom_name(elem)

    # Get the input
    input_text = helper.extract_value_from_string_or_dict(elem, 'WFImage')
    if input_text is None:
        input_text = ''

    res = {'Get Frames from': input_text}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
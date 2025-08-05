import parse_xml.parse_shortcut_WF as helper


def action_url_expand(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Expand': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output name if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the input
    input_text = helper.extract_value_from_string_or_dict(elem, 'URL')

    res = {'Expand': input_text}
    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
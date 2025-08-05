import parse_xml.parse_shortcut_WF as helper


def action_open_safariview(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Open': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.track_custom_name(elem)

    # Get the URL
    url = helper.extract_value_from_string_or_dict(elem, 'target')
    if url is None:
        url = ''

    res = {'Open': url}
    if custom_output_name is not None:
        res['Output Name'] = custom_output_name
    return helper.append_data(res, uuid)
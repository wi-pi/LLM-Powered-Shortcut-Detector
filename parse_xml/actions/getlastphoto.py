import parse_xml.parse_shortcut_WF as helper


def action_getlastphoto(elem):
    if elem.tag == 'dict' and len(elem) == 0:
        return helper.append_data({'Get the latest': '1 photo', 'Include Screenshots': True}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.track_custom_name(elem)

    # Get the count
    count = helper.extract_value_from_string_or_dict(elem, 'WFGetLatestPhotoCount')
    if count is None:
        count = '1 photo'
    else:
        count = helper.list_to_str(count)
        count = f"{count} photos"

    # Get the include screenshots
    include_screenshots = helper.get_elements_after_key(elem, 'WFGetLatestPhotosActionIncludeScreenshots', 'false')
    if include_screenshots is None:
        include_screenshots = True
    else:
        include_screenshots = False

    res = {'Get the latest': count, 'Include Screenshots': include_screenshots}
    if custom_output_name is not None:
        res['Custom Output Name'] = custom_output_name
    return helper.append_data(res, uuid)

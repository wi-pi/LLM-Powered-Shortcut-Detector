import parse_xml.parse_shortcut_WF as helper


def action_format_filesize(elem):
    if not helper.check_validation(elem):
        raise ValueError('Invalid Format File Size action.')

    # Track the UUID
    uuid = helper.track_uuid(elem)

    # Find if the element has custom output name
    custom_output_name = helper.track_custom_name(elem)

    # Find the format size-could be a string or a dict after WFFileSize
    format_size = helper.extract_value_from_string_or_dict(elem, 'WFFileSize')
    if format_size is None:
        format_size = ''

    # Find the size format - could be a string or a dict after WFFileSizeFormat
    size_format = helper.extract_value_from_string_or_dict(elem, 'WFFileSizeFormat')
    if size_format is None:
        size_format = 'Closest Unit'

    res = {
        'Format': format_size,
        'Into': size_format
    }

    # Find include unit or not
    if size_format != 'Closest Unit':
        include_unit = helper.get_elements_after_key(elem, 'WFFileSizeIncludeUnits', 'false')
        if include_unit is not None:
            include_unit = False
        else:
            include_unit = True
        res['Include Units'] = include_unit

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
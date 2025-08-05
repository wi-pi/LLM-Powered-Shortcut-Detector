import parse_xml.parse_shortcut_WF as helper


def action_makezip(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Make': '', 'archive from': '', 'Archive Name': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output name if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the make type input
    make_type = helper.extract_value_from_string_or_dict(elem, 'WFArchiveFormat')
    if make_type is None:
        make_type = '.zip'

    # Get the from input
    from_input = helper.extract_value_from_string_or_dict(elem, 'WFInput')
    if from_input is None:
        from_input = ''

    # Get the archive name
    archive_name = helper.extract_value_from_string_or_dict(elem, 'WFZIPName')
    if archive_name is None:
        archive_name = ''

    res = {'Make': make_type, 'archive from': from_input, 'Archive Name': archive_name}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
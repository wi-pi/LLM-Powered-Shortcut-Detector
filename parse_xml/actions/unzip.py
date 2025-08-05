import parse_xml.parse_shortcut_WF as helper


def action_unzip(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Extract': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output name if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the from input
    from_input = helper.extract_value_from_string_or_dict(elem, 'WFArchive')
    if from_input is None:
        from_input = ''

    res = {'Extract': from_input}
    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
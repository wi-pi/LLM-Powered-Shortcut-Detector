import parse_xml.parse_shortcut_WF as helper


def action_geturlcomponent(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Get': '', 'from': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output name if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the get type input
    get_type = helper.extract_value_from_string_or_dict(elem, 'WFURLComponent')
    if get_type is None:
        get_type = 'Scheme'

    # Get the from input
    from_input = helper.extract_value_from_string_or_dict(elem, 'WFURL')
    if from_input is None:
        from_input = ''

    res = {'Get': get_type, 'from': from_input}
    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
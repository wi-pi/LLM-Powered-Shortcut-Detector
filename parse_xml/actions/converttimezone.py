import parse_xml.parse_shortcut_WF as helper


def action_converttimezone(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Input Time': '', 'From': '', 'To': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    res = {}

    # Find if the element have custom output name
    custom_output_name = helper.get_elements_after_key(elem, 'CustomOutputName', 'string')
    if custom_output_name is not None:
        custom_output_name = custom_output_name[0].text

    # Get the input date -- WFInput
    input_date = helper.extract_value_from_string_or_dict(elem, 'Date')
    if input_date is None:
        input_date = ''

    res['Input Time'] = input_date


    from_zone = ''
    to_zone = ''
    # Get the timezone to convert from -- SourceTimeZone
    from_elem = helper.get_elements_after_key(elem, 'SourceTimeZone', 'dict')
    if from_elem is not None:
        # Case 1 it is user selected input, case 2 it is a predefined timezone
        zone = helper.get_elements_after_key(from_elem[0], 'timeZone', 'string')
        if zone is not None:
            from_zone = zone[0].text
        else:
            from_zone = helper.get_final_value(from_elem[0])
            from_zone = helper.get_attachments_by_range(from_zone)

    # Get the timezone to convert to -- DestinationTimeZone
    dest_elem = helper.get_elements_after_key(elem, 'DestinationTimeZone', 'dict')
    if dest_elem is not None:
        # Case 1 it is user selected input, case 2 it is a predefined timezone
        zone = helper.get_elements_after_key(dest_elem[0], 'timeZone', 'string')
        if zone is not None:
            to_zone = zone[0].text
        else:
            to_zone = helper.get_final_value(dest_elem[0])
            to_zone = helper.get_attachments_by_range(to_zone)

    res['From'] = from_zone
    res['To'] = to_zone

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
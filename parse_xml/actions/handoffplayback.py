import parse_xml.parse_shortcut_WF as helper


def action_handoffplayback(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Hand off playback from': '', 'to': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the source
    source = helper.get_elements_after_key(elem, 'WFSourceMediaRoute', 'dict')
    if source is not None:
        source_elem = helper.get_elements_after_key(source[0], 'isLocalDevice', 'true')
        if source_elem is not None:
            source = 'iPhone Speaker'
        else:
            source = helper.extract_value_from_string_or_dict(elem, 'WFSourceMediaRoute')
    else:
        source = ''

    # Get the destination
    destination = helper.get_elements_after_key(elem, 'WFDestinationMediaRoute', 'dict')
    if destination is not None:
        destination_elem = helper.get_elements_after_key(destination[0], 'isLocalDevice', 'true')
        if destination_elem is not None:
            destination = 'iPhone Speaker'
        else:
            destination = helper.extract_value_from_string_or_dict(elem, 'WFDestinationMediaRoute')
    else:
        destination = ''

    res = {'Hand off playback from': source, 'to': destination}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
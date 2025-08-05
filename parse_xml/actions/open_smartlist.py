import parse_xml.parse_shortcut_WF as helper


def action_open_smartlist(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Open': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # Get what to open
    open = helper.get_elements_after_key(elem, 'targetEntity', 'dict')
    if open is not None:
        open = helper.get_elements_after_key(open[0], 'title', 'dict')
        if open is None:
            open = helper.extract_value_from_string_or_dict(elem, 'targetEntity')
        else:
            open = helper.extract_value_from_string_or_dict(open[0], 'key')
    if open is None:
        open = ''

    res = {'Open': open}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name
    return helper.append_data(res, uuid)
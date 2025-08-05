import parse_xml.parse_shortcut_WF as helper


def action_opentab(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Open': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output name if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the open input
    open_input = helper.extract_value_from_string_or_dict(elem, 'tab')
    if open_input is None:
        open_input = ''

    res = {'Open': open_input}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name
    return helper.append_data(res, uuid)
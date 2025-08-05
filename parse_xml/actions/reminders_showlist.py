import parse_xml.parse_shortcut_WF as helper


def action_reminders_showlist(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Open': 'Reminders'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # Get what to open
    open = helper.get_elements_after_key(elem, 'WFList', 'dict')
    if open is not None:
        open = helper.extract_value_from_string_or_dict(open[0], 'Title')
        if open is None:
            open = helper.extract_value_from_string_or_dict(elem, 'WFList')
    if open is None:
        open = 'Reminders'

    res = {'Open': open}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name
    return helper.append_data(res, uuid)
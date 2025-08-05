import parse_xml.parse_shortcut_WF as helper


def action_removereminders(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Remove': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # Get what to remove
    remove = helper.extract_value_from_string_or_dict(elem, 'WFInputReminders')
    if remove is None:
        remove = ''

    res = {'Remove': remove}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name
    return helper.append_data(res, uuid)
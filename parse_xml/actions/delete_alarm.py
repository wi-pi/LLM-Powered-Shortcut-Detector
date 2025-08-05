import parse_xml.parse_shortcut_WF as helper


def action_delete_alarm(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Delete': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output name if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the alarm time
    repeat_list = []
    repeat_elem = helper.get_elements_after_key(elem, 'entities', 'array')
    if repeat_elem is not None:
        for item in repeat_elem[0]:
            repeat_list.append(helper.extract_value_from_string_or_dict(item, 'title'))
    else:
        repeat_list = helper.extract_value_from_string_or_dict(elem, 'entities')

    res = {'Delete': repeat_list}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)


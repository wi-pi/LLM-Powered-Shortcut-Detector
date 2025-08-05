import parse_xml.parse_shortcut_WF as helper


def action_set_personalhotspot(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Set Personal Hotspot password to': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    output_name = helper.track_custom_name(elem)

    input = helper.extract_value_from_string_or_dict(elem, 'WFInput')
    if input is None:
        input = ''

    res = {'Set Personal Hotspot password to': input}

    if output_name is not None:
        res['Output Name'] = output_name

    return helper.append_data(res, uuid)
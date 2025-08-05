import parse_xml.parse_shortcut_WF as helper


def action_getbatterylevel(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Get Info': 'Battery Level'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.get_elements_after_key(elem, 'CustomOutputName', 'string')
    if custom_output_name is not None:
        custom_output_name = custom_output_name[0].text

    # Get the battery level type
    battery_level_type = helper.extract_value_from_string_or_dict(elem, 'Subject')
    if battery_level_type is None:
        battery_level_type = 'Battery Level'
    res = {'Get Info': battery_level_type}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
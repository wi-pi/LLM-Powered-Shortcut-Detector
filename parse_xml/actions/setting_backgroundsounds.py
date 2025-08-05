import parse_xml.parse_shortcut_WF as helper


def action_setting_backgroundsounds(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Set Background Sounds': 'Volume', 'to': '10%'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the item to set
    item = helper.extract_value_from_string_or_dict(elem, 'volumeType')
    if item is None:
        item = 'Volume'
    else:
        item = helper.list_to_str(item)

    # Get the value
    value = helper.extract_value_from_string_or_dict(elem, 'volumeValue')
    if value is None:
        value = '10%'
    else:
        value = f"{helper.list_to_str(value)} %"

    res = {'Set Background Sounds': item, 'to': value}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
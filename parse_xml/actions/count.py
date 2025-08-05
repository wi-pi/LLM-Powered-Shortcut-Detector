import parse_xml.parse_shortcut_WF as helper


def action_count(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Count': 'Items', 'in': ''}, None)

    # Check for UUID
    uuid = helper.track_uuid(elem)

    # Check for custom output name
    custom_output_name = helper.track_custom_name(elem)

    # Get the data of counting (always a dict after key Input)
    data_count = ''
    data_dict = helper.get_elements_after_key(elem, 'Input', 'dict')
    if data_dict is not None:
        data_count = helper.get_final_value(data_dict[0])
        data_count = helper.get_attachments_by_range(data_count)

    # Format of counting -- could be either a string or a dict
    format_count = 'Items'
    format_count_elem = helper.extract_value_from_string_or_dict(elem, 'WFCountType')
    if format_count_elem is not None:
        format_count = format_count_elem

    ret_dict = {
        'Count': format_count,
        'in': data_count,
    }

    if custom_output_name is not None:
        ret_dict['Custom Output Name'] = custom_output_name
    return helper.append_data(ret_dict, uuid)

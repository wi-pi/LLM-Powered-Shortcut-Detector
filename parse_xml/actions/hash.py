import parse_xml.parse_shortcut_WF as helper


def action_hash(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Hash Type': 'MD5', 'Input': ''}, None)

    # Track the UUID
    uuid = helper.track_uuid(elem)

    # Find if the element has custom output name
    custom_output_name = helper.track_custom_name(elem)

    # Find the hash type
    hash_type = helper.extract_value_from_string_or_dict(elem, 'WFHashType')
    if hash_type is None:
        hash_type = 'MD5'

    # Find the input data
    data = ''
    data_elem = helper.get_elements_after_key(elem, 'WFInput', 'dict')
    if data_elem is not None:
        data_elem = helper.get_final_value(data_elem[0])
        data = helper.get_attachments_by_range(data_elem)

    res = {
        'Hash Type': hash_type,
        'Input': data
    }

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
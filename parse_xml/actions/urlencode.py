import parse_xml.parse_shortcut_WF as helper


def action_urlencode(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Encode Type': 'Encode', 'Input': ''}, None)

    # Track the UUID
    uuid = helper.track_uuid(elem)

    # Find if the element has custom output name
    custom_output_name = helper.track_custom_name(elem)

    # Find the encode type
    encode_type = helper.extract_value_from_string_or_dict(elem, 'WFEncodeMode')
    if encode_type is None:
        encode_type = 'Encode'

    # Find the input data
    data_elem = helper.extract_value_from_string_or_dict(elem, 'WFInput')
    if data_elem is None:
        data_elem = ''
    else:
        if len(data_elem) == 0:
            data_elem = ''

    res = {
        'Encode Type': encode_type,
        'Input': data_elem
    }

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
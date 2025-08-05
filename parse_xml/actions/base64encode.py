import parse_xml.parse_shortcut_WF as helper


def action_base64encode(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'input': '', 'Encode Mode': 'Encode', 'Line breaks at': 'Every 76 characters'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.get_elements_after_key(elem, 'CustomOutputName', 'string')
    if custom_output_name is not None:
        custom_output_name = custom_output_name[0].text

    # Get Encode Mode, ir could be string or dict
    encode_mode = 'Encode'
    encode_mode_elem = helper.get_elements_after_key(elem, 'WFEncodeMode', 'string')
    if encode_mode_elem is not None:
        encode_mode = encode_mode_elem[0].text
    else:
        encode_mode_elem = helper.get_elements_after_key(elem, 'WFEncodeMode', 'dict')
        if encode_mode_elem is not None:
            encode_mode_elem = helper.get_final_value(encode_mode_elem[0])
            encode_mode = helper.get_attachments_by_range(encode_mode_elem)

    # Get the line break at, it could be string or dict
    line_break_at = 'Every 76 characters'
    line_break_at_elem = helper.get_elements_after_key(elem, 'WFBase64LineBreakMode', 'string')
    if line_break_at_elem is not None:
        line_break_at = line_break_at_elem[0].text
    else:
        line_break_at_elem = helper.get_elements_after_key(elem, 'WFBase64LineBreakMode', 'dict')
        if line_break_at_elem is not None:
            line_break_at_elem = helper.get_final_value(line_break_at_elem[0])
            line_break_at = helper.get_attachments_by_range(line_break_at_elem)

    # Get the input to encode -- always under WFInput and in a dict
    encode_input = ''
    input_dict = helper.get_elements_after_key(elem, 'WFInput', 'dict')
    if input_dict is not None:
        input_dict = helper.get_final_value(input_dict[0])
        encode_input = helper.get_attachments_by_range(input_dict)

    if encode_mode == 'Encode':
        if custom_output_name is not None:
            return helper.append_data({'input': encode_input, 'Encode Mode': 'Encode', 'Line breaks at': line_break_at, 'Custom Output Name': custom_output_name}, uuid)
        return helper.append_data({'input': encode_input, 'Encode Mode': 'Encode', 'Line breaks at': line_break_at}, uuid)
    else:
        if custom_output_name is not None:
            return helper.append_data({'input': encode_input, 'Encode Mode': encode_mode, 'Custom Output Name': custom_output_name}, uuid)
        return helper.append_data({'input': encode_input, 'Encode Mode': encode_mode}, uuid)
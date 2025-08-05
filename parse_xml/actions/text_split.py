import parse_xml.parse_shortcut_WF as helper


def action_text_split(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Split': '', 'by': 'New Lines'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.get_elements_after_key(elem, 'CustomOutputName', 'string')
    if custom_output_name is not None:
        custom_output_name = custom_output_name[0].text

    # Get the input to split -- always an array or a dict or a string that is under <key>text<key>
    split_input = ''
    input_dict = helper.get_elements_after_key(elem, 'text', 'dict')
    # case 1: input is a dict -- there is an attachment
    if input_dict is not None:
        input_dict = helper.get_final_value(input_dict[0])
        split_input = helper.get_attachments_by_range(input_dict)
    # case 2: input is an array -- there is no attachment but multiple values
    else:
        input_array = helper.get_elements_after_key(elem, 'text', 'array')
        if input_array is not None:
            # Each item in an array is either a string or a dict
            input_array = input_array[0]
            for item in input_array:
                if item is not None:
                    if item.tag == 'string':
                        if item.text is not None:
                            split_input += item.text + '\n'
                    elif item.tag == 'dict':
                        item = helper.get_final_value(item)
                        tmp = helper.get_attachments_by_range(item)
                        if tmp is not None:
                            split_input += str(tmp) + '\n'
        # case 3: input is a string
        else:
            input_string = helper.get_elements_after_key(elem, 'text', 'string')
            if input_string is not None:
                split_input = input_string[0].text

    general_separator = 'New Lines'
    # Get general separator, if has one, it could be a string or a dict
    separator_elem = helper.get_elements_after_key(elem, 'WFTextSeparator', 'string')
    if separator_elem is not None:
        general_separator = separator_elem[0].text
        if general_separator == 'Custom':
            # Could be string or dict
            separator_elem = helper.get_elements_after_key(elem, 'WFTextCustomSeparator', 'string')
            if separator_elem is not None:
                general_separator = separator_elem[0].text
            else:
                separator_elem = helper.get_elements_after_key(elem, 'WFTextCustomSeparator', 'dict')
                if separator_elem is not None:
                    separator_elem = helper.get_final_value(separator_elem[0])
                    general_separator = helper.get_attachments_by_range(separator_elem)
    else:
        separator_elem = helper.get_elements_after_key(elem, 'WFTextSeparator', 'dict')
        if separator_elem is not None:
            separator_elem = helper.get_final_value(separator_elem[0])
            general_separator = helper.get_attachments_by_range(separator_elem)

    if custom_output_name is not None:
        return helper.append_data(
            {'Split': split_input, 'by': general_separator, 'Custom Output Name': custom_output_name}, uuid)
    return helper.append_data({'Split': split_input, 'by': general_separator}, uuid)

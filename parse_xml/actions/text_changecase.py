import parse_xml.parse_shortcut_WF as helper


def action_text_changecase(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Input': '', 'Case Type': 'UPPERCASE'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.get_elements_after_key(elem, 'CustomOutputName', 'string')
    if custom_output_name is not None:
        custom_output_name = custom_output_name[0].text

    # Get the input -- array or string or dict after text
    input_text = []
    input_text_elem = helper.extract_value_from_string_or_dict(elem, 'text')
    if input_text_elem is None:
        input_text_elem = helper.get_elements_after_key(elem, 'text', 'array')
        if input_text_elem is not None:
            if len(input_text_elem[0]) == 0:
                input_text = []
            else:
                for item in input_text_elem[0]:
                    # Could be a dict or a string
                    if item.tag == 'dict':
                        item = helper.get_final_value(item)
                        input_text.append(helper.get_attachments_by_range(item))
                    else:
                        input_text.append(item.text)
        else:
            input_text = []
    else:
        input_text = [input_text_elem]

    # Get the case type
    case_type = helper.extract_value_from_string_or_dict(elem, 'WFCaseType')
    if case_type is None:
        case_type = 'UPPERCASE'

    res = {'Input': input_text, 'Case Type': case_type}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)


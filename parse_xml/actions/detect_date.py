import parse_xml.parse_shortcut_WF as helper


def action_detect_date(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Get dates from': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    res = {}

    # Find if the element have custom output name
    custom_output_name = helper.track_custom_name(elem)

    # Get the input text -- WFInput
    input_text = helper.get_elements_after_key(elem, 'WFInput', 'dict')
    if input_text is None:
        input_text = ''
    else:
        input_text = helper.get_final_value(input_text[0])
        input_text = helper.get_attachments_by_range(input_text)

    res['Get dates from'] = input_text

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
import parse_xml.parse_shortcut_WF as helper


def action_detect_text(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Get text from': ''}, None)

    # Find if the element have custom output name
    custom_output_name = helper.track_custom_name(elem)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the input of the action -- must be a dict
    input_text = ''
    input_text_elem = helper.get_elements_after_key(elem, 'WFInput', 'dict')
    if input_text_elem is not None:
        input_text_elem = helper.get_final_value(input_text_elem[0])
        input_text = helper.get_attachments_by_range(input_text_elem)

    if custom_output_name is not None:
        return helper.append_data({'Get text from': input_text, 'Custom Output Name': custom_output_name}, uuid)

    return helper.append_data({'Get text from': input_text}, uuid)

import parse_xml.parse_shortcut_WF as helper


def action_appendvariable(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Add': '', 'to': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.track_custom_name(elem)

    # Get the variable name
    variable_name = ''
    variable_name_elem = helper.get_elements_after_key(elem, 'WFVariableName', 'string')
    if variable_name_elem is not None:
        variable_name = variable_name_elem[0].text

    # Get the input of the action -- must be a dict
    input_text = ''
    input_text_elem = helper.get_elements_after_key(elem, 'WFInput', 'dict')
    if input_text_elem is not None:
        input_text_elem = helper.get_final_value(input_text_elem[0])
        input_text = helper.get_attachments_by_range(input_text_elem)

    res = {'Add': input_text, 'to': variable_name}
    if custom_output_name is not None:
        res['Output Name'] = custom_output_name
    return helper.append_data(res, uuid)

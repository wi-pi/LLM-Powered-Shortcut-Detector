import parse_xml.parse_shortcut_WF as helper


def action_repeat_each(elem):
    if not helper.check_validation(elem):
        return ''

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.get_elements_after_key(elem, 'CustomOutputName', 'string')
    if custom_output_name is not None:
        custom_output_name = custom_output_name[0].text

    metalist = {}
    # Check Group Identifier
    group_identifier = helper.get_elements_after_key(elem, 'GroupingIdentifier', 'string')
    if group_identifier is not None:
        group_identifier = group_identifier[0].text
        metalist['Group Identifier'] = group_identifier
    else:
        raise ValueError('GroupIdentifier not found in Repeat Each action')

    # Get control flow -- repeat item or end repeat line
    control_flow = helper.get_elements_after_key(elem, 'WFControlFlowMode', 'integer')
    if control_flow is not None:
        control_flow = control_flow[0].text
        if control_flow == '0':
            metalist['Action'] = 'Repeat with each item in'
        elif control_flow == '2':
            metalist['Action'] = 'End Repeat'
        else:
            raise ValueError('WFControlFlowMode not found in Repeat Each action')
    else:
        raise ValueError('WFControlFlowMode not found in Repeat Each action')

    if control_flow == '2':
        if custom_output_name is not None:
            metalist['Output Name'] = custom_output_name
        return {'metadata': metalist}, {'uuid': uuid}

    # Get input -- it is always a dict after WFInput
    input_text = ''
    input_text_elem = helper.get_elements_after_key(elem, 'WFInput', 'dict')
    if input_text_elem is not None:
        input_text_elem = helper.get_final_value(input_text_elem[0])
        input_text = helper.get_attachments_by_range(input_text_elem)

    # Find if the element have custom output name
    custom_output_name = helper.get_elements_after_key(elem, 'CustomOutputName', 'string')
    if custom_output_name is not None:
        custom_output_name = custom_output_name[0].text

    # Get the input of the action -- must be a dict
    input_text = ''
    input_text_elem = helper.get_elements_after_key(elem, 'WFInput', 'dict')
    if input_text_elem is not None:
        input_text_elem = helper.get_final_value(input_text_elem[0])
        input_text = helper.get_attachments_by_range(input_text_elem)

    return {'metadata': metalist}, helper.append_data(input_text, uuid)

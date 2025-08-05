import parse_xml.parse_shortcut_WF as helper



def action_repeat_count(elem):
    if not helper.check_validation(elem):
        raise ValueError('Validation failed in Repeat Count action')

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.get_elements_after_key(elem, 'CustomOutputName', 'string')
    if custom_output_name is not None:
        custom_output_name = custom_output_name[0].text

    res_list = {}

    # Track the Group Identifier
    group_identifier = helper.get_metadata(elem, 'GroupingIdentifier')
    if group_identifier is None:
        raise ValueError('GroupingIdentifier is not found in the conditional action.')
    res_list['Group Identifier'] = group_identifier

    # Get control flow -- repeat item or end repeat line
    control_flow = helper.get_elements_after_key(elem, 'WFControlFlowMode', 'integer')
    if control_flow is not None:
        control_flow = control_flow[0].text
        if control_flow == '0':
            res_list['Action'] = 'Repeat'
            # Get repeat count
            repeat_count_elem = helper.get_elements_after_key(elem, 'WFRepeatCount', 'integer')
            if repeat_count_elem is not None:
                repeat_count = repeat_count_elem[0].text
                res_list['Repeat Count'] = repeat_count
            else:
                repeat_count_elem = helper.get_elements_after_key(elem, 'WFRepeatCount', 'real')
                if repeat_count_elem is not None:
                    repeat_count = repeat_count_elem[0].text
                    res_list['Repeat Count'] = repeat_count
                else:
                    # In client version 411, it could be user input
                    repeat_count_elem = helper.get_elements_after_key(elem, 'WFRepeatCount', 'dict')
                    if repeat_count_elem is not None:
                        repeat_count_elem = helper.get_final_value(repeat_count_elem[0])
                        repeat_count = helper.get_attachments_by_range(repeat_count_elem)
                        res_list['Repeat Count'] = repeat_count
                    else:
                        repeat_count = '1'
                        res_list['Repeat Count'] = repeat_count
        elif control_flow == '2':
            res_list['Action'] = 'End Repeat'
    else:
        raise ValueError('WFControlFlowMode not found in Repeat Each action')

    if custom_output_name is not None:
        res_list['Output Name'] = custom_output_name

    return helper.append_data(res_list, uuid)
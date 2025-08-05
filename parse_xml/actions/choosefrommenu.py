import parse_xml.parse_shortcut_WF as helper



def action_choosefrommenu(elem):
    if not helper.check_validation(elem):
        raise ValueError('Invalid Choose from Menu action')

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
        raise ValueError('GroupIdentifier not found in choose from menu action')

    # Get control flow -- prompt.txt vs items vs ending
    control_flow = helper.get_elements_after_key(elem, 'WFControlFlowMode', 'integer')
    if control_flow is not None:
        control_flow = control_flow[0].text
        if control_flow == '0':
            metalist['Prompt'] = 'Choose from menu with'
        elif control_flow == '2':
            metalist['Prompt'] = 'End Menu'
            if custom_output_name is not None:
                metalist['Output Name'] = custom_output_name
        elif control_flow == '1':
            title_elem = helper.get_elements_after_key(elem, 'WFMenuItemTitle', 'string')
            if title_elem is not None:
                title_elem = title_elem[0].text
                if title_elem is None:
                    title_elem = ''
                metalist['Prompt'] = title_elem
            # else:
                # raise ValueError('WFMenuItemTitle not found in choose from menu action')
        else:
            raise ValueError('Unexpected value in WFControlFlowMode')
    else:
        raise ValueError('WFControlFlowMode not found in choose from menu action')

    # Get menu items text from controlflow == 0
    if control_flow == '0':
        menu_list = []
        # The manu should be in an array
        menu_arr = helper.get_elements_after_key(elem, 'WFMenuItems', 'array')
        if menu_arr is not None:
            menu_arr = menu_arr[0]
            for menu_item in menu_arr:
                # Each item in this array is a string or a dict
                if menu_item.tag == 'string':
                    if menu_item.text is None:
                        menu_list.append('')
                    else:
                        menu_list.append(menu_item.text)
                elif menu_item.tag == 'dict':
                    dict_element = helper.get_elements_after_key(menu_item, 'WFValue', 'dict')
                    if dict_element is not None:
                        if dict_element[0][0].tag == 'key' and dict_element[0][0].text == 'Synonyms':
                            list_data = []
                            arr_elem = helper.get_elements_after_key(dict_element[0], 'Synonyms', 'array')
                            for item in arr_elem[0]:
                                list_data.append(helper.get_attachments_by_range(item))
                        else:
                            dict_element = helper.get_final_value(dict_element[0])
                            menu_list.append(helper.get_attachments_by_range(dict_element))
                else:
                    raise ValueError('Unexpected type in menu items')
        else:
            menu_list = ['One', 'Two']
        metalist['Menu Items'] = menu_list
        metalist['Prompt'] = 'Choose from menu with'

    if custom_output_name is not None:
        metalist['Output Name'] = custom_output_name

    return helper.append_data(metalist, uuid)


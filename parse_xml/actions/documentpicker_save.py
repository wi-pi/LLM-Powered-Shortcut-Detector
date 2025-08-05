import parse_xml.parse_shortcut_WF as helper


def action_documentpicker_save(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Save': '', 'to': 'Shortcuts', 'Ask Where to Save': True, 'Overwrite If File Exists': False}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output name if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the from input
    from_input = ''
    parse_elem = helper.get_elements_after_key(elem, 'WFInput', 'dict')
    if parse_elem is not None:
        from_input = helper.parse_file_input(parse_elem[0], 'WFInput')
    if from_input is None:
        from_input = ''

    # Get the to input (folder)
    to_input = helper.get_elements_after_key(elem, 'WFFolder', 'dict')
    if to_input is not None:
        to_input = helper.parse_file_input(to_input[0], 'WFFolder')
    else:
        to_input = 'Shortcuts'

    # Get the ask where to save
    ask_where_to_save = helper.get_elements_after_key(elem, 'WFAskWhereToSave', 'false')
    if ask_where_to_save is not None:
        ask_where_to_save = False
    else:
        ask_where_to_save = True

    res = {'Save': from_input, 'to': to_input, 'Ask Where to Save': ask_where_to_save}

    if not ask_where_to_save:
        # get the sub path
        sub_path = helper.extract_value_from_string_or_dict(elem, 'WFFileDestinationPath')
        if sub_path is None:
            sub_path = ''
        res['Subpath'] = sub_path

    # Get the overwrite if file exists
    overwrite_if_file_exists = helper.get_elements_after_key(elem, 'WFSaveFileOverwrite', 'true')
    if overwrite_if_file_exists is not None:
        overwrite_if_file_exists = True
    else:
        overwrite_if_file_exists = False

    res['Overwrite If File Exists'] = overwrite_if_file_exists

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
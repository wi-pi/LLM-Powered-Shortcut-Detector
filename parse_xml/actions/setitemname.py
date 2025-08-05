import parse_xml.parse_shortcut_WF as helper


def action_setitemname(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Set Name of': '', 'to': '', 'Dont Include File Extension': False}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.track_custom_name(elem)

    # Get the input of the action -- must be a dict
    ret_actions = helper.extract_value_from_string_or_dict(elem, 'WFInput')
    if ret_actions is None:
        ret_actions = ''

    res = {'Set Name of': ret_actions}

    # Get set name to what
    to_name = helper.extract_value_from_string_or_dict(elem, 'WFName')
    if to_name is None:
        to_name = ''
    res['to'] = to_name

    # Get dont include file extension boolean
    dont_include_file_extension = helper.get_elements_after_key(elem, 'WFDontIncludeFileExtension', 'true')
    if dont_include_file_extension is not None:
        dont_include_file_extension = True
    else:
        dont_include_file_extension = False

    res['Dont Include File Extension'] = dont_include_file_extension

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
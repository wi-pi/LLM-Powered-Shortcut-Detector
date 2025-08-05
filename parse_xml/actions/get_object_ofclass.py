import parse_xml.parse_shortcut_WF as helper


def action_get_object_ofclass(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Get object of class': '', 'from': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    get = helper.extract_value_from_string_or_dict(elem, 'Class')
    if get is None:
        get = ''

    of_class = helper.extract_value_from_string_or_dict(elem, 'Input')
    if of_class is None:
        of_class = ''

    res = {'Get object of class': get, 'from': of_class}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name
    return helper.append_data(res, uuid)
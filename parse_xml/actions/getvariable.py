import parse_xml.parse_shortcut_WF as helper


def action_getvariable(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Get': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the variable name
    variable_name = ''
    variable_name_elem = helper.get_elements_after_key(elem, 'WFVariable', 'dict')
    if variable_name_elem is not None:
        variable_name_elem = helper.get_final_value(variable_name_elem[0])
        variable_name = helper.get_attachments_by_range(variable_name_elem)

    res = {'Get': variable_name}

    return helper.append_data(res, uuid)
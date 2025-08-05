import parse_xml.parse_shortcut_WF as helper


def action_getitemtype(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Get Type of': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.track_custom_name(elem)

    # Get the input of the action -- must be a dict
    ret_actions = helper.extract_value_from_string_or_dict(elem, 'WFInput')
    if ret_actions is None:
        ret_actions = ''

    res = {'Get Type of': ret_actions}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
import parse_xml.parse_shortcut_WF as helper


def action_viewresult(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'View Content Graph of': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    custom_name = helper.track_custom_name(elem)

    # Get the input of the action -- must be a dict
    ret_actions = helper.extract_value_from_string_or_dict(elem, 'WFInput')
    if ret_actions is None:
        ret_actions = ''

    res = {'View Content Graph of': ret_actions}

    if custom_name:
        res['Output Name'] = custom_name

    return helper.append_data(ret_actions, uuid)
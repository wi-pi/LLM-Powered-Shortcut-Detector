import parse_xml.parse_shortcut_WF as helper


def action_getmyworkflows(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Get Shortcuts from': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    custom_name = helper.track_custom_name(elem)

    # Get the input of the action -- must be a dict
    ret_actions = helper.get_elements_after_key(elem, 'Folder', 'dict')
    if ret_actions is None:
        ret_actions = ''
    else:
        if ret_actions[0][0].text == 'DisplayString':
            ret_actions = ret_actions[0][1].text + '(folder)'
        else:
            ret_actions = helper.get_final_value(ret_actions[0])
            ret_actions = helper.get_attachments_by_range(ret_actions)

    res = {'Get Shortcuts from': ret_actions}

    if custom_name:
        res['Output Name'] = custom_name

    return helper.append_data(res, uuid)
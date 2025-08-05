import parse_xml.parse_shortcut_WF as helper


def action_getitemname(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Get Name of': '', 'Get Web Page Title': True}, None)
    # Check UUID
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.track_custom_name(elem)

    # Get the input of the action -- must be a dict
    ret_actions = helper.get_elements_after_key(elem, 'WFInput', 'dict')
    if ret_actions is None:
        ret_actions = ''
    else:
        ret_actions = helper.get_final_value(ret_actions[0])
        ret_actions = helper.get_attachments_by_range(ret_actions)

    res = {'Get Name of': ret_actions}
    # Get web page title boolean
    get_web_page_title = helper.get_elements_after_key(elem, 'GetWebPageTitle', 'false')
    if get_web_page_title is not None:
        get_web_page_title = False
    else:
        get_web_page_title = True
    res['Get Web Page Title'] = get_web_page_title

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
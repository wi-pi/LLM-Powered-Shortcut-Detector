import parse_xml.parse_shortcut_WF as helper

def action_gettext(elem):
    """
    Extracts the 'Get Text' action from the action.

    Parameters:
    - elem (Element): The XML element containing the 'Get Text' action.

    Returns:
    - The 'Get Text' action string.
    """
    if not helper.check_validation(elem):
        return helper.append_data({'Text': ''}, None)
    uuid = helper.track_uuid(elem)
    ret_actions = helper.extract_value_from_string_or_dict(elem, 'WFTextActionText')
    if ret_actions is None:
        # in case there is no 'WFTextActionText' key in the dictionary
        ret_actions = ''
    res = {'Text': ret_actions}
    return helper.append_data(res, uuid)

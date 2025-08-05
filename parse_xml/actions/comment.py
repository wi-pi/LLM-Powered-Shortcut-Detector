import parse_xml.parse_shortcut_WF as helper


def action_comment(elem):
    """
    Extracts the comment from the action.

    Parameters:
    - elm (Element): The XML element containing the comment.

    Returns:
    - The comment string.
    """
    if not helper.check_validation(elem):
        return helper.append_data('', None)
    uuid = helper.track_uuid(elem)
    # No attachments
    ret_actions = helper.get_elements_after_key(elem, 'WFCommentActionText', 'string')
    if ret_actions is None:
        # in case there is no 'WFCommentActionText' key in the dictionary
        if not helper.check_if_key_exist(elem, 'WFCommentActionText'):
            ret_actions = ''
        else:
            # Have attachments
            dic = helper.get_elements_after_key(elem, 'WFCommentActionText', 'dict')
            value_elem = helper.get_final_value(dic[0])
            ret_actions = helper.get_attachments_by_range(value_elem)
    else:
        ret_actions = ret_actions[0].text

    return helper.append_data(ret_actions, uuid)
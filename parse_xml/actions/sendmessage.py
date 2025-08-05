import parse_xml.parse_shortcut_WF as helper
import base64



def action_sendmessage(elem, client_number):
    if not helper.check_validation(elem):
        return helper.append_data({'Send': '', 'to': '', 'Show When Run': True}, None)
    # Check UUID
    uuid = helper.track_uuid(elem)

    # Check if the message appear on user's screen when the shortcut is running
    show_when_run = True
    show_when_run_elem = helper.get_elements_after_key(elem, 'WFShowWhenRun', 'true')
    if show_when_run_elem is None:
        show_when_run_elem = helper.get_elements_after_key(elem, 'WFShowWhenRun', 'false')
        if show_when_run_elem is not None:
            show_when_run = False

    # Get the message
    # Message could be string or dict
    message = helper.get_elements_after_key(elem, 'WFSendMessageContent', 'string')
    message = '' if message is None else message[0].text
    if message == '':
        # Might be an attachment/Dictionary
        message = helper.get_elements_after_key(elem, 'WFSendMessageContent', 'dict')
        if message is not None:
            message_dic = helper.get_final_value(message[0])
            message = helper.get_attachments_by_range(message_dic)
        else:
            message = ''

    # Get the recipients
    recipients_dic = helper.get_elements_after_key(elem, 'WFSendMessageActionRecipients', 'dict')
    content_list = []
    if recipients_dic is not None:
        content_list = helper.parse_contact_info(recipients_dic[0], client_number)
        # recipients_dic = helper.get_final_value(recipients_dic[0])
        # data_dic = helper.get_elements_after_key(recipients_dic, 'WFContactFieldValues', 'array')
        # if data_dic is None:
        #     # Special case? Is it because version number = 900?
        #     content_list.append(helper.get_attachments_by_range(recipients_dic))
        #     res = {'Message': message, 'Recipients': content_list, 'Show When Run': show_when_run}
        #     return helper.append_data(res, uuid)
        #     # raise ValueError('No recipient found while parsing the send message action')



    res = {'Send': message, 'to': content_list, 'Show When Run': show_when_run}
    return helper.append_data(res, uuid)

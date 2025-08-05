import parse_xml.parse_shortcut_WF as helper
from parse_xml_output.parse_output_to_natural_language import parse_get_attachment


def action_change_focus_mail(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Set Mail Focus Filter while in': 'Do Not Disturb', 'Accounts': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output name if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the action
    action = helper.extract_value_from_string_or_dict(elem, 'Mode')
    if action is None:
        action = 'Set'
    else:
        action = helper.list_to_str(action)

    # Get the focus filter
    focus_filter = helper.get_elements_after_key(elem, 'FocusMode', 'dict')
    if focus_filter is not None:
        focus_filter = helper.extract_value_from_string_or_dict(focus_filter[0], 'DisplayString')
        if focus_filter is None:
            focus_filter = helper.extract_value_from_string_or_dict(elem, 'FocusMode')
            if focus_filter is None: raise ValueError('FocusMode not found')
    else:
        focus_filter = 'Do Not Disturb'

    res = {f'{action} Mail Focus Filter while in': focus_filter}

    # if the action is set, get the accounts
    if action == 'Set':
        # Get the account
        account_list = []
        account_elem = helper.get_elements_after_key(elem, 'accounts', 'array')
        if account_elem is not None:
            for account in account_elem[0]:
                cur = helper.get_elements_after_key(account, 'title', 'dict')
                account_list.append(helper.extract_value_from_string_or_dict(cur[0], 'key'))
        else:
            cur_elem = helper.get_elements_after_key(elem, 'accounts', 'dict')
            if cur_elem is not None:
                cur_elem = helper.get_elements_after_key(cur_elem[0], 'title', 'dict')
                if cur_elem is not None:
                    account_list = helper.extract_value_from_string_or_dict(cur_elem[0], 'key')
                else:
                    account_list = helper.extract_value_from_string_or_dict(elem, 'accounts')
            else:
                account_list = ''
        res['Accounts'] = account_list

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
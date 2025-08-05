import parse_xml.parse_shortcut_WF as helper


def action_note_openaccount(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Open the Account': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the account
    account = ''
    account_elem = helper.get_elements_after_key(elem, 'target', 'dict')
    if account_elem is not None:
        account = helper.parse_note(account_elem[0])

    res = {'Open the Account': account}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name
    return helper.append_data(res, uuid)
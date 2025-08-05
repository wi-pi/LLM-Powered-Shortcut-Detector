import parse_xml.parse_shortcut_WF as helper


def action_venmo_pay(elem, client_number):
    if not helper.check_validation(elem):
        return helper.append_data({'Send': ' USD', 'to': '', 'App': 'Apple Pay', 'Open in App': False, 'Note': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the amount + unit
    amount = helper.get_elements_after_key(elem, 'WFVenmoActionAmount', 'dict')
    if amount is None:
        amount = ' USD'
    else:
        amount_elem = helper.get_final_value(amount[0])
        amount = helper.extract_value_from_string_or_dict(amount_elem, 'Magnitude')
        if amount is None:
            amount = ''
        unit = helper.extract_value_from_string_or_dict(amount_elem, 'Unit')
        if unit is None:
            unit = 'USD'
        amount = f'{amount} {unit}'

    # Get the recipient
    recipient = helper.get_elements_after_key(elem, 'WFVenmoActionRecipients', 'dict')
    if recipient is not None:
        recipient = helper.parse_contact_info(recipient[0], client_number)
    else:
        recipient = ''

    # Get the app
    app = helper.get_elements_after_key(elem, 'IntentAppDefinition', 'dict')
    if app is not None:
        app = helper.extract_value_from_string_or_dict(app[0], 'Name')
        if app is None:
            raise ValueError('App name is not found')
    else:
        app = 'Apple Pay'

    # Get the open in app
    open_in_app = helper.get_elements_after_key(elem, 'WFVenmoActionAppSwitch', 'true')
    if open_in_app is None:
        open_in_app = False
    else:
        open_in_app = True

    # Get the note
    note = helper.extract_value_from_string_or_dict(elem, 'WFVenmoActionNote')
    if note is None:
        note = ''

    res = {'Send': amount, 'to': recipient, 'App': app, 'Open in App': open_in_app, 'Note': note}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
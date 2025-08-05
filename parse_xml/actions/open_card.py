import parse_xml.parse_shortcut_WF as helper


def action_open_card(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Open': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the card
    card = ''
    card_elem = helper.get_elements_after_key(elem, 'target', 'dict')
    if card_elem is not None:
        card_elem = helper.get_elements_after_key(card_elem[0], 'title', 'dict')
        if card_elem is not None:
            card = helper.extract_value_from_string_or_dict(card_elem[0], 'key')
        else:
            card = helper.extract_value_from_string_or_dict(elem, 'target')

    if card is None:
        card = ''

    res = {'Open': card}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
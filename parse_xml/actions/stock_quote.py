import parse_xml.parse_shortcut_WF as helper


def action_stock_quote(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Open Stock Quote': 'NASDAQ'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    stock = helper.get_elements_after_key(elem, 'target', 'dict')
    if stock is not None:
        stock = helper.extract_value_from_string_or_dict(stock[0], 'identifier')
        if stock is None:
            stock = helper.extract_value_from_string_or_dict(elem, 'target')
    if stock is None:
        stock = 'NASDAQ'

    res = {'Open Stock Quote': stock}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name
    return helper.append_data(res, uuid)
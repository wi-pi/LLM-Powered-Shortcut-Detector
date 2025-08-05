import parse_xml.parse_shortcut_WF as helper


def action_rss(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Get': 'items', 'from': 'https://www.apple.com/newsroom/rss-feed.rss'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.track_custom_name(elem)

    res = {}

    # Get the items
    items = helper.get_elements_after_key(elem, 'WFRSSItemQuantity', 'real')
    if items is not None:
        items = items[0].text
        res['Get'] = 'items'
        res['RSS #'] = items
    else:
        items = helper.get_elements_after_key(elem, 'WFRSSItemQuantity', 'dict')
        if items is not None:
            items = helper.get_final_value(items[0])
            items = helper.get_attachments_by_range(items)
            res['Get'] = items
        else:
            items = '1'
            res['Get'] = 'items'
            res['RSS #'] = items

    # Get the input
    input_text = helper.extract_value_from_string_or_dict(elem, 'WFRSSFeedURL')
    if input_text is None:
        input_text = 'https://www.apple.com/newsroom/rss-feed.rss'

    res['from'] = input_text

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
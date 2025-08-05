import parse_xml.parse_shortcut_WF as helper


def action_setting_develpersetting(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Find': 'All Developer Settings', 'Limit': False}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the things to filter
    filter = helper.extract_value_from_string_or_dict(elem, 'WFContentItemInputParameter')
    if filter is None:
        filter = 'All Developer Settings'

    # Get the limit
    limit = helper.get_elements_after_key(elem, 'WFContentItemLimitEnabled', 'true')
    if limit is not None:
        limit = True
    else:
        limit = False

    res = {'Find': filter, 'Limit': limit}

    if limit:
        limit_num = helper.get_elements_after_key(elem, 'WFContentItemLimitNumber', 'real')
        if limit_num is not None:
            res['Get # of items'] = limit_num[0].text
        else:
            res['Get # of items'] = '5.0'

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
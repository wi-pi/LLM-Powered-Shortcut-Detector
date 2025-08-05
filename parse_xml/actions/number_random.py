import parse_xml.parse_shortcut_WF as helper


def action_number_random(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Min': '', 'Max': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.track_custom_name(elem)

    res = {}

    # Get the number
    min_num = helper.extract_value_from_string_or_dict(elem, 'WFRandomNumberMinimum')
    if min_num is None:
        min_num = ''

    res['Min'] = min_num

    max_num = helper.extract_value_from_string_or_dict(elem, 'WFRandomNumberMaximum')
    if max_num is None:
        max_num = ''

    res['Max'] = max_num

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)

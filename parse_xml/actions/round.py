import parse_xml.parse_shortcut_WF as helper


def action_round(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Round number': '', 'Decimal Place': '','Mode': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.get_elements_after_key(elem, 'CustomOutputName', 'string')
    if custom_output_name is not None:
        custom_output_name = custom_output_name[0].text

    res = {}

    # Get the number
    number = helper.extract_value_from_string_or_dict(elem, 'WFInput')
    if number is None:
        number = ''

    res['Round number'] = number

    # Get the decimal places
    decimal_places = helper.extract_value_from_string_or_dict(elem, 'WFRoundTo')
    if decimal_places is None:
        decimal_places = 'Ones Place'

    res['Decimal Places'] = decimal_places

    # Get the mode
    mode = helper.extract_value_from_string_or_dict(elem, 'WFRoundMode')
    if mode is None:
        mode = 'Normal'

    res['Mode'] = mode

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
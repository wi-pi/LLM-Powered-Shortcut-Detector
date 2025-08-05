import parse_xml.parse_shortcut_WF as helper


def action_format_number(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Format': '', 'to': '2 decimal places'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    output_name = helper.track_custom_name(elem)

    number = helper.extract_value_from_string_or_dict(elem, 'WFNumber')
    if number is None:
        number = ''

    decimal = helper.extract_value_from_string_or_dict(elem, 'WFNumberFormatDecimalPlaces')
    if decimal is None:
        decimal = '2 decimal places'

    res = {'Format': number, 'to': decimal}

    if output_name is not None:
        res['Output Name'] = output_name

    return helper.append_data(res, uuid)
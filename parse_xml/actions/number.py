import parse_xml.parse_shortcut_WF as helper


def action_number(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Number':''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.track_custom_name(elem)

    res = {}

    # Get the number
    number = helper.extract_value_from_string_or_dict(elem, 'WFNumberActionNumber')
    if number is None:
        number = ''

    res['Number'] = number

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
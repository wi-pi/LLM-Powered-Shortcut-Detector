import parse_xml.parse_shortcut_WF as helper


def action_calculateexpression(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Calculate expression': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    output_name = helper.track_custom_name(elem)

    expression = helper.extract_value_from_string_or_dict(elem, 'Input')

    if expression is None:
        expression = ''

    res = {'Calculate expression': expression}

    if output_name is not None:
        res['Output Name'] = output_name

    return helper.append_data(res, uuid)
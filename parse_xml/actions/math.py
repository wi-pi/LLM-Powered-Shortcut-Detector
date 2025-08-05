import parse_xml.parse_shortcut_WF as helper


def action_math(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Input 1': '', 'Operation': '+', 'Input 2': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    output_name = helper.track_custom_name(elem)

    input1 = helper.extract_value_from_string_or_dict(elem, 'WFInput')
    if input1 is None:
        input1 = ''

    operation = helper.extract_value_from_string_or_dict(elem, 'WFMathOperation')
    if operation is None:
        operation = '+'

    input2 = helper.extract_value_from_string_or_dict(elem, 'WFMathOperand')
    if input2 is None:
        input2 = ''

    res = {'Input 1': input1, 'Operation': operation, 'Input 2': input2}

    if output_name is not None:
        res['Output Name'] = output_name

    return helper.append_data(res, uuid)
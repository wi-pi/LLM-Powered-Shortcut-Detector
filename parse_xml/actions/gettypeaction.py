import parse_xml.parse_shortcut_WF as helper


def action_gettypeaction(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Get type of': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    number = helper.extract_value_from_string_or_dict(elem, 'WFInput')
    if number is None:
        number = ''

    res = {'Get type of': number}


    if custom_output_name is not None:
        res['Output Name'] = custom_output_name
    return helper.append_data(res, uuid)
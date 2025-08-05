import parse_xml.parse_shortcut_WF as helper


def action_showinstore(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Show in iTunes Store': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    app = helper.extract_value_from_string_or_dict(elem, 'WFProduct')
    if app is None:
        app = ''

    res = {'Show in iTunes Store': app}


    if custom_output_name is not None:
        res['Output Name'] = custom_output_name
    return helper.append_data(res, uuid)
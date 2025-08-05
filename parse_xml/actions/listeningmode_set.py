import parse_xml.parse_shortcut_WF as helper


def action_listeningmode_set(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Set Noise Control mode on': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the mode
    mode = helper.extract_value_from_string_or_dict(elem, 'WFListeningMode')
    if mode is None:
        mode = ''

    res = {'Set Noise Control mode on': mode}

    if mode != '':
        # Get the to value
        route = helper.extract_value_from_string_or_dict(elem, 'WFRoute')
        res['to'] = route

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
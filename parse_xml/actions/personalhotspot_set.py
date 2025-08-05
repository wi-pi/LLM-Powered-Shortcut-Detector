import parse_xml.parse_shortcut_WF as helper


def action_personalhotspot_set(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Action': 'Turn', 'State': 'On'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    if uuid is not None:
        raise ValueError('UUID is not None for personal hotspot set')

    output_name = helper.track_custom_name(elem)


    res = helper.interpret_turn_toggle(elem)

    if output_name is not None:
        res['Output Name'] = output_name

    return helper.append_data(res, None)
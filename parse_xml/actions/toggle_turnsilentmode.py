import parse_xml.parse_shortcut_WF as helper


def action_toggle_turnsilentmode(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Action': 'Turn', 'State': 'On'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    output_name = helper.track_custom_name(elem)

    res = helper.interpret_turn_toggle(elem)
    if output_name is not None:
        res['Output Name'] = output_name

    return helper.append_data(res, uuid)
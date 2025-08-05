import parse_xml.parse_shortcut_WF as helper


def action_show_quicknote(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Action': 'Show Quick Note'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    res = {'Action': 'Show Quick Note'}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name
    return helper.append_data(res, uuid)
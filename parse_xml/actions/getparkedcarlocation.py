import parse_xml.parse_shortcut_WF as helper


def action_getparkedcarlocation(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Text': 'Get Parked Car Location'}, helper.track_uuid(elem))

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output name if have
    custom_output_name = helper.track_custom_name(elem)

    if custom_output_name is not None:
        return helper.append_data({'Text': 'Get Parked Car Location', 'Output Name': custom_output_name}, uuid)

    return helper.append_data({'Text': 'Get Parked Car Location'}, uuid)

import parse_xml.parse_shortcut_WF as helper


def action_savetocameraroll(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Save': '', 'to': 'Recents'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # get what to save
    save_image = helper.extract_value_from_string_or_dict(elem, 'WFInput')
    if save_image is None:
        save_image = ''

    # get to where to save
    save_to_album = helper.extract_value_from_string_or_dict(elem, 'WFCameraRollSelectedGroup')
    if save_to_album is None:
        save_to_album = 'Recents'

    res = {'Save': save_image, 'to': save_to_album}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
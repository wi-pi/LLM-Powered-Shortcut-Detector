import parse_xml.parse_shortcut_WF as helper


def action_removefromalbum(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Remove': '', 'from': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # get what to remove
    remove_image = helper.extract_value_from_string_or_dict(elem, 'WFInput')
    if remove_image is None:
        remove_image = ''

    # get from where to remove
    remove_from_album = helper.extract_value_from_string_or_dict(elem, 'WFRemoveAlbumSelectedGroup')
    if remove_from_album is None:
        remove_from_album = ''

    res = {'Remove': remove_image, 'from': remove_from_album}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
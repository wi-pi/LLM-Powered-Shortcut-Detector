import parse_xml.parse_shortcut_WF as helper


def action_photo_createalbum(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Create Album': '', 'with photo': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    name = helper.extract_value_from_string_or_dict(elem, 'AlbumName')
    if name is None:
        name = ''

    photo = helper.extract_value_from_string_or_dict(elem, 'WFInput')
    if photo is None:
        photo = ''

    res = {'Create Album': name, 'with photo': photo}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name
    return helper.append_data(res, uuid)
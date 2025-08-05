import parse_xml.parse_shortcut_WF as helper


def action_deletephoto(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Delete': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # get what to delete
    delete_image = ''
    delete_elem = helper.get_elements_after_key(elem, 'photos', 'array')
    if delete_elem is not None:
        for elem in delete_elem[0]:
            delete_image += elem.text + ', '
    else:
        delete_image = helper.extract_value_from_string_or_dict(elem, 'photos')
        if delete_image is None:
            delete_image = ''

    res = {'Delete': delete_image}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
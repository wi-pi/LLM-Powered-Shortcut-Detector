import parse_xml.parse_shortcut_WF as helper


def action_recognize_music(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Add to Library': True, 'Error If Not Recognized': False}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    add_lib = helper.get_elements_after_key(elem, 'addToLibrary', 'false')
    if add_lib is not None:
        add_lib = False
    else:
        add_lib = True

    error = helper.get_elements_after_key(elem, 'errorIfNotRecognized', 'true')
    if error is not None:
        error = True
    else:
        error = False

    res = {'Add to Library': add_lib, 'Error If Not Recognized': error}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name
    return helper.append_data(res, uuid)
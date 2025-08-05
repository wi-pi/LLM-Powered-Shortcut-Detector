import parse_xml.parse_shortcut_WF as helper


def action_trimvideo(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Trim': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # get what to save
    save_image = helper.extract_value_from_string_or_dict(elem, 'WFInputMedia')
    if save_image is None:
        save_image = ''

    res = {'Trim': save_image}


    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
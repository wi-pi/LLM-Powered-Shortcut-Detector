import parse_xml.parse_shortcut_WF as helper


def action_takescreenshot(elem):
    if not helper.check_validation(elem):
        return helper.append_data('', None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.get_elements_after_key(elem, 'CustomOutputName', 'string')
    if custom_output_name is not None:
        custom_output_name = custom_output_name[0].text

    if custom_output_name is not None:
        return helper.append_data({'Output Name': custom_output_name}, uuid)


    return helper.append_data('', uuid)
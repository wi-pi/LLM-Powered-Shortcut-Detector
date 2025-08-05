import parse_xml.parse_shortcut_WF as helper


def action_properties_music(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Get': 'Artist', 'from': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # Get what to get
    what = helper.extract_value_from_string_or_dict(elem, 'WFContentItemPropertyName')
    if what is None:
        what = 'Artist'

    # Get the music
    music = helper.extract_value_from_string_or_dict(elem, 'WFInput')
    if music is None:
        music = ''

    res = {'Get': what, 'from': music}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name
    return helper.append_data(res, uuid)
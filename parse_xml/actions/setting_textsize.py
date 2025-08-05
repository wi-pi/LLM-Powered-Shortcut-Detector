import parse_xml.parse_shortcut_WF as helper


def action_setting_textsize(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Set text size to': 'Extra Small'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the text size
    size = helper.extract_value_from_string_or_dict(elem, 'textSize')
    if size is None:
        size = 'Extra Small'

    res = {'Set text size to': size}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
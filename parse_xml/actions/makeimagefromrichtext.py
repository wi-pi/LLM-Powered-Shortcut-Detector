import parse_xml.parse_shortcut_WF as helper


def action_makeimagefromrichtext(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Make image from': '', 'Width': '1024', 'Height': '768'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output name if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the input
    input_text = helper.extract_value_from_string_or_dict(elem, 'WFInput')
    if input_text is None:
        input_text = ''

    # Get the width
    width = helper.extract_value_from_string_or_dict(elem, 'WFWidth')
    if width is None:
        width = '1024'

    # Get the height
    height = helper.extract_value_from_string_or_dict(elem, 'WFHeight')
    if height is None:
        height = '768'

    res = {'Make image from': input_text, 'Width': width, 'Height': height}
    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
import parse_xml.parse_shortcut_WF as helper


def action_makeimagefrompdfpage(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Make': 'PNG image', 'from': '', 'Color': 'RGB', 'Resolution (dots per inch)': '300'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output name if have
    custom_output_name = helper.track_custom_name(elem)

    # Get what to make
    format_input = helper.extract_value_from_string_or_dict(elem, 'WFMakeImageFromPDFPageImageFormat')
    if format_input is None:
        format_input = 'PNG image'

    # Get the input
    input_text = helper.extract_value_from_string_or_dict(elem, 'WFInput')
    if input_text is None:
        input_text = ''

    # Get the color
    color = helper.extract_value_from_string_or_dict(elem, 'WFMakeImageFromPDFPageColorspace')
    if color is None:
        color = 'RGB'

    # Get the resolution
    resolution = helper.extract_value_from_string_or_dict(elem, 'WFMakeImageFromPDFPageResolution')
    if resolution is None:
        resolution = '300'

    res = {'Make': format_input, 'from': input_text, 'Color': color, 'Resolution (dots per inch)': resolution}
    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
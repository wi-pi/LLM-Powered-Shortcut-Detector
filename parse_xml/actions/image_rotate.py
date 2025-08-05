import parse_xml.parse_shortcut_WF as helper
import parse_xml_output.parse_output_to_natural_language as parse_output

def action_image_rotate(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Rotate': '', 'by': '90 degrees'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.track_custom_name(elem)

    # Get the input
    input_text = helper.extract_value_from_string_or_dict(elem, 'WFImage')
    if input_text is None:
        input_text = ''

    # Get the by
    by = helper.extract_value_from_string_or_dict(elem, 'WFImageRotateAmount')
    if by is None:
        by = '90 degrees'
    else:
        if type(by) == list:
            by = parse_output.parse_get_attachment(by)
        by = f"{by} degrees"

    res = {'Rotate': input_text, 'by': by}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
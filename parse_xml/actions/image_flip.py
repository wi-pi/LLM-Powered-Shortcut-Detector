import parse_xml.parse_shortcut_WF as helper


def action_image_flip(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Flip': 'Choose', '': 'Horizontally'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output name if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the flip input
    flip = helper.extract_value_from_string_or_dict(elem, 'WFInput')
    if flip is None:
        flip = ''

    # Get the direction
    input_text = helper.extract_value_from_string_or_dict(elem, 'WFImageFlipDirection')
    if input_text is None:
        input_text = 'Horizontally'

    res = {'Flip': flip, '': input_text}
    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
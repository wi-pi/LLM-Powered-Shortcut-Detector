import parse_xml.parse_shortcut_WF as helper


def action_image_crop(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Crop': '', 'Position': 'Center', 'Width': '100', 'Height': '100'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output name if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the input
    input = helper.extract_value_from_string_or_dict(elem, 'WFInput')
    if input is None:
        input = ''

    # Get the position
    position = helper.extract_value_from_string_or_dict(elem, 'WFImageCropPosition')
    if position is None:
        position = 'Center'

    res = {'Crop': input, 'Position': position}

    if position == 'Custom':
        # Get x and y coordinates
        x = helper.extract_value_from_string_or_dict(elem, 'WFImageCropX')
        if x is None:
            x = ''
        y = helper.extract_value_from_string_or_dict(elem, 'WFImageCropY')
        if y is None:
            y = ''
        res['X Coordinate'] = x
        res['Y Coordinate'] = y

    # Get the width
    width = helper.extract_value_from_string_or_dict(elem, 'WFImageCropWidth')
    if width is None:
        width = '100'

    res['Width'] = width

    # Get the height
    height = helper.extract_value_from_string_or_dict(elem, 'WFImageCropHeight')
    if height is None:
        height = '100'

    res['Height'] = height

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
import parse_xml.parse_shortcut_WF as helper


def action_image_mask(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Mask': '', 'with': 'Rounded Rectangle', 'shape':'', 'Corner Radius': '0'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output name if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the mask input
    mask = helper.extract_value_from_string_or_dict(elem, 'WFInput')
    if mask is None:
        mask = ''

    # Get the mask shape
    mask_image = helper.extract_value_from_string_or_dict(elem, 'WFMaskType')
    if mask_image is None:
        mask_image = 'Rounded Rectangle'

    res = {'Mask': mask, 'with': mask_image, 'shape': ''}

    # Get radius of the mask is rounded rectangle
    if mask_image == 'Rounded Rectangle':
        corner_radius = helper.extract_value_from_string_or_dict(elem, 'WFMaskCornerRadius')
        if corner_radius is None:
            corner_radius = '0'
        res['Corner Radius'] = corner_radius
    elif mask_image == 'Custom Image':
        mask_shape = helper.extract_value_from_string_or_dict(elem, 'WFCustomMaskImage')
        if mask_shape is not None:
            # mask_shape = ''
            res[''] = mask_shape

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
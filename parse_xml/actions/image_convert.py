import parse_xml.parse_shortcut_WF as helper


def action_image_convert(elem):
    if elem.tag == 'dict' and len(elem) == 0:
        return helper.append_data({'Convert': '', 'to': 'JPEG', 'Quality': '70.0', 'Preserve Metadata': True}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.get_elements_after_key(elem, 'CustomOutputName', 'string')
    if custom_output_name is not None:
        custom_output_name = custom_output_name[0].text

    # Get if the metadata should be preserved
    preserve_metadata = True
    preserve_metadata_elem = helper.get_elements_after_key(elem, 'WFImagePreserveMetadata', 'false')
    if preserve_metadata_elem is not None:
        preserve_metadata = False

    # Get image to convert, it will be a dict after the key WFInput
    image = ''
    image_dict = helper.get_elements_after_key(elem, 'WFInput', 'dict')
    if image_dict is not None:
        image_dict = helper.get_final_value(image_dict[0])
        image = helper.get_attachments_by_range(image_dict)

    # Get the format -- it could be a string, or a dict
    format_to_convert = 'JPEG'
    format_elem = helper.get_elements_after_key(elem, 'WFImageFormat', 'string')
    if format_elem is not None:
        format_to_convert = format_elem[0].text
    else:
        format_elem = helper.get_elements_after_key(elem, 'WFImageFormat', 'dict')
        if format_elem is not None:
            format_elem = helper.get_final_value(format_elem[0])
            format_to_convert = helper.get_attachments_by_range(format_elem)

    # Get the quality
    quality = '70.0'
    quality_elem = helper.get_elements_after_key(elem, 'WFImageCompressionQuality', 'real')
    if quality_elem is not None:
        quality = quality_elem[0].text

    # Report result according to their type
    if format_to_convert == 'JPEG':
        if custom_output_name is not None:
            return helper.append_data({'Convert': image, 'to': 'JPEG', 'Quality': quality, 'Preserve Metadata': preserve_metadata, 'Custom Output Name': custom_output_name}, uuid)
        return helper.append_data({'Convert': image, 'to': 'JPEG', 'Quality': quality, 'Preserve Metadata': preserve_metadata},
                                  uuid)
    elif format_to_convert in ['PNG', 'HEIF', 'TIFF', 'Match Input']:
        if custom_output_name is not None:
            return helper.append_data({'Convert': image, 'to': format_to_convert, 'Preserve Metadata': preserve_metadata, 'Custom Output Name': custom_output_name}, uuid)
        return helper.append_data({'Convert': image, 'to': format_to_convert, 'Preserve Metadata': preserve_metadata}, uuid)
    else:
        if custom_output_name is not None:
            return helper.append_data({'Convert': image, 'to': format_to_convert, 'Custom Output Name': custom_output_name}, uuid)
        return helper.append_data({'Convert': image, 'to': format_to_convert}, uuid)


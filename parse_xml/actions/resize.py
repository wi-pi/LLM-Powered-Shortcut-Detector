import parse_xml.parse_shortcut_WF as helper


def action_resize(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Resize': '', 'to': 'Size', 'Width': '640', 'Height': 'Auto Height'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.track_custom_name(elem)

    image = ''
    # Get image to resize -- it must be an image? It must. But the actual value could be other thing -- like a string
    image_dict = helper.get_elements_after_key(elem, 'WFImage', 'dict')
    if image_dict is not None:
        image_dict = helper.get_final_value(image_dict[0])
        image = helper.get_attachments_by_range(image_dict)

    resize_mode = 'Size'
    # Get the resize mode -- this could be a string -- by default, the size. Or it could be a dictionary
    resize_mode_dict = helper.get_elements_after_key(elem, 'WFImageResizeKey', 'string')
    if resize_mode_dict is not None:
        resize_mode = resize_mode_dict[0].text
    else:
        resize_mode_dict = helper.get_elements_after_key(elem, 'WFImageResizeKey', 'dict')
        if resize_mode_dict is not None:
            resize_mode_dict = helper.get_final_value(resize_mode_dict[0])
            resize_mode = helper.get_attachments_by_range(resize_mode_dict)

    # Get the width and height
    if resize_mode == 'Longest Edge':
        main_scale_elem = helper.get_elements_after_key(elem, 'WFImageResizeLength', 'string')
        # It can also be a dictionary
        main_scale = '640'
        if main_scale_elem is None:
            main_scale_elem = helper.get_elements_after_key(elem, 'WFImageResizeLength', 'dict')
            if main_scale_elem is not None:
                main_scale = helper.get_final_value(main_scale_elem[0])
                main_scale = helper.get_attachments_by_range(main_scale)
        else:
            main_scale = main_scale_elem[0].text
        res = {'Resize': image, 'to': resize_mode, 'Length': main_scale}
        if custom_output_name is not None:
            res['Custom Output Name'] = custom_output_name
        return helper.append_data(res, uuid)
    elif resize_mode == 'Percentage':
        percentage = '100'
        percentage_elem = helper.get_elements_after_key(elem, 'WFImageResizePercentage', 'string')
        if percentage_elem is None:
            percentage_elem = helper.get_elements_after_key(elem, 'WFImageResizePercentage', 'dict')
            if percentage_elem is not None:
                percentage = helper.get_final_value(percentage_elem[0])
                percentage = helper.get_attachments_by_range(percentage)
        else:
            percentage = percentage_elem[0].text
        res = {'Resize': image, 'to': resize_mode, 'Percentage': percentage}
        if custom_output_name is not None:
            res['Custom Output Name'] = custom_output_name
        return helper.append_data(res, uuid)
    elif resize_mode == 'Size':
        width = '640'
        height = 'Auto Height'
        width_elem = helper.get_elements_after_key(elem, 'WFImageResizeWidth', 'string')
        height_elem = helper.get_elements_after_key(elem, 'WFImageResizeHeight', 'string')
        if width_elem is None:
            width_elem = helper.get_elements_after_key(elem, 'WFImageResizeWidth', 'dict')
            if width_elem is not None:
                width = helper.get_final_value(width_elem[0])
                width = helper.get_attachments_by_range(width)
        else:
            width = width_elem[0].text
        if height_elem is None:
            height_elem = helper.get_elements_after_key(elem, 'WFImageResizeHeight', 'dict')
            if height_elem is not None:
                height = helper.get_final_value(height_elem[0])
                height = helper.get_attachments_by_range(height)
        else:
            height = height_elem[0].text
        res = {'Resize': image, 'to': resize_mode, 'Width': width, 'Height': height}
        if custom_output_name is not None:
            res['Custom Output Name'] = custom_output_name
        return helper.append_data(res, uuid)
    else:
        res = {'Resize': image, 'to': resize_mode}
        if custom_output_name is not None:
            res['Custom Output Name'] = custom_output_name

        return helper.append_data(res, uuid)

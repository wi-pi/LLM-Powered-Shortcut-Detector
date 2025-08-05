import parse_xml.parse_shortcut_WF as helper


def action_overlaytext(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Overlay': '', 'on': '', 'at': '', 'Font': 'System', 'Font Size': '10%', 'Text Alignment': 'Center', 'Font Color': 'White', 'Rotation': '0', 'Outline Text': False, 'Maximum Width': '80%', 'Sizing': 'Proportional'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output name if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the text
    overlay_text = helper.extract_value_from_string_or_dict(elem, 'WFText')
    if overlay_text is None:
        overlay_text = ''

    # Get the over image
    overlay_image = helper.extract_value_from_string_or_dict(elem, 'WFImage')
    if overlay_image is None:
        overlay_image = ''

    # Get the position
    position = helper.extract_value_from_string_or_dict(elem, 'WFTextPosition')
    if position is None:
        position = 'Center'

    res = {'Overlay': overlay_text, 'on': overlay_image, 'at': position}
    # Get the sizing method
    sizing = helper.extract_value_from_string_or_dict(elem, 'WFSizingMethod')
    if sizing is None:
        sizing = 'Proportional'
    if position == 'Custom Position':
        # Get the x and y coordinates if position is custom
        x = helper.extract_value_from_string_or_dict(elem, 'WFTextX')
        if x is None:
            x = '0'

        y = helper.extract_value_from_string_or_dict(elem, 'WFTextY')
        if y is None:
            y = '0'
        res[''] = f"{x},{y}"
    elif position != 'Center':

        if sizing == 'Proportional':
            offset = helper.extract_value_from_string_or_dict(elem, 'WFPercentageTextOffset')
            if offset is None:
                offset = 0.1
            res['offset by'] = f"{offset * 100}%"
        elif sizing == 'Absolute':
            offset = helper.extract_value_from_string_or_dict(elem, 'WFTextOffset')
            if offset is None:
                offset = 0
            res['offset by'] = f"{offset} points"
        else:
            res['offset by'] = "points"

    # # Get the font
    # font_elem = helper.get_elements_after_key(elem, 'WFFont', 'dict')
    # if font_elem is None:
    #     font = 'System'
    # else:
    #     font = helper.get_elements_after_key(font_elem[0], 'WFFontDescriptorFamily', 'string')
    #     if font is None:
    #         font = helper.get_elements_after_key(font_elem[0], 'WFFontDescriptorName', 'string')
    #         if font is None:
    #             raise ValueError('Font not found')
    #     else:
    #         font = helper.extract_value(font[0])
    #
    # res['Font'] = font

    # Get the font size
    font_size = helper.extract_value_from_string_or_dict(elem, 'WFFontSize')
    if font_size is None:
        font_size = '0.1'
    if sizing == 'Proportional' or sizing == 'Absolute':
        res['Font Size'] = font_size

    # Get the text alignment
    text_alignment = helper.extract_value_from_string_or_dict(elem, 'WFTextAlignment')
    if text_alignment is None:
        text_alignment = 'Center'

    res['Text Alignment'] = text_alignment

    # Get the font color
    rgb = ''
    xml_data = helper.get_elements_after_key(elem, 'WFTextColor', 'dict')
    if xml_data is None:
        rgb = 'White'
    else:
        xml_data = xml_data[0]
        red = helper.extract_value_from_string_or_dict(xml_data, 'redComponent')
        green = helper.extract_value_from_string_or_dict(xml_data, 'greenComponent')
        blue = helper.extract_value_from_string_or_dict(xml_data, 'blueComponent')

        # Return RGB tuple
        rgb = (red, green, blue)

    res['Font Color'] = rgb

    # Get the rotation
    rotation = helper.extract_value_from_string_or_dict(elem, 'WFTextRotation')
    if rotation is None:
        rotation = '0'

    res['Rotation'] = rotation

    # Get the outline text
    outline_text = helper.get_elements_after_key(elem, 'WFTextOutlineEnabled', 'true')
    if outline_text is None:
        outline_text = False
    else:
        outline_text = True

    res['Outline Text'] = outline_text

    # If the outline text is true, get
    # stroke width and stroke color
    if outline_text:
        # Get the stroke width
        stroke_width = None
        if sizing == 'Absolute':
            stroke_width = helper.extract_value_from_string_or_dict(elem, 'WFTextStrokeWidth')
            if stroke_width is None:
                stroke_width = '0'
        elif sizing == 'Proportional':
            stroke_width = helper.extract_value_from_string_or_dict(elem, 'WFPercentageTextStrokeWidth')
            if stroke_width is None:
                stroke_width = '0.1'
        if stroke_width is not None:
            res['Stroke Width'] = stroke_width

        # Get the stroke color
        stroke_color = helper.get_elements_after_key(elem, 'WFTextStrokeColor', 'dict')
        if stroke_color is None:
            stroke_color = 'White'
        else:
            xml_data = stroke_color[0]
            red = helper.extract_value_from_string_or_dict(xml_data, 'redComponent')
            green = helper.extract_value_from_string_or_dict(xml_data, 'greenComponent')
            blue = helper.extract_value_from_string_or_dict(xml_data, 'blueComponent')

            # Return RGB tuple
            stroke_color = (red, green, blue)

        res['Stroke Color'] = stroke_color

    # Get the maximum width
    if sizing == 'Absolute':
        max_width = helper.extract_value_from_string_or_dict(elem, 'WFTextBoxWidth')
        if max_width is None:
            max_width = '0'
        res['Maximum Width'] = max_width
    elif sizing == 'Proportional':
        max_width = helper.extract_value_from_string_or_dict(elem, 'WFPercentageTextBoxWidth')
        if max_width is None:
            max_width = 0.8
        res['Maximum Width'] = f"{max_width * 100}%"

    res['Sizing'] = sizing


    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
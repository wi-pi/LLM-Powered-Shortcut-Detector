import parse_xml.parse_shortcut_WF as helper


def action_overlayimageonimage(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Overlay': '', 'on': '', 'Show Image Editor': True}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output name if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the overlay image
    overlay_image = helper.extract_value_from_string_or_dict(elem, 'WFImage')
    if overlay_image is None:
        overlay_image = ''

    # Get the over image
    over_image = helper.extract_value_from_string_or_dict(elem, 'WFInput')
    if over_image is None:
        over_image = ''

    # get the show image editor
    show_editor = helper.get_elements_after_key(elem, 'WFShouldShowImageEditor', 'false')
    if show_editor is None:
        show_editor = True
    else:
        show_editor = False

    res = {'Overlay': overlay_image, 'on': over_image, 'Show Image Editor': show_editor}

    # Get parameters if show editor is false
    if not show_editor:
        # Get the position
        position = helper.extract_value_from_string_or_dict(elem, 'WFImagePosition')
        if position is None:
            position = 'Center'

        res['Position'] = position

        # Get the width
        width = helper.extract_value_from_string_or_dict(elem, 'WFImageWidth')
        if width is None:
            width = 'Auto'

        res['Width'] = width

        # Get the height
        height = helper.extract_value_from_string_or_dict(elem, 'WFImageHeight')
        if height is None:
            height = 'Auto'

        res['Height'] = height

        # Get the x and y coordinates if position is custom
        if position == 'Custom':
            x = helper.extract_value_from_string_or_dict(elem, 'WFImageX')
            if x is None:
                x = '0'
            y = helper.extract_value_from_string_or_dict(elem, 'WFImageY')
            if y is None:
                y = '0'
            res['X Coordinate'] = x
            res['Y Coordinate'] = y

        # Get the rotation
        rotation = helper.extract_value_from_string_or_dict(elem, 'WFRotation')
        if rotation is None:
            rotation = '0'

        res['Rotation'] = rotation

        # Get the opacity
        opacity = helper.extract_value_from_string_or_dict(elem, 'WFOverlayImageOpacity')
        if opacity is None:
            opacity = '100'

        res['Opacity'] = opacity

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
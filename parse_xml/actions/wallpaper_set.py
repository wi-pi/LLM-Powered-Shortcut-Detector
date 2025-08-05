import parse_xml.parse_shortcut_WF as helper


def action_wallpaper_set(elem):
    if not helper.check_validation(elem):
        raise ValueError('Invalid Set Wallpaper action')

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.get_elements_after_key(elem, 'CustomOutputName', 'string')
    if custom_output_name is not None:
        custom_output_name = custom_output_name[0].text

    # Get the wallpaper to be changed
    wallpaper = ''
    wallpaper_name_elem = helper.get_elements_after_key(elem, 'WFSelectedPoster', 'dict')
    if wallpaper_name_elem is not None:
        wall_uuid = helper.track_uuid(wallpaper_name_elem[0])
        wallpaper_name = helper.get_elements_after_key(wallpaper_name_elem[0], 'name', 'string')
        if wallpaper_name is None:
            wallpaper_name = ''
        else:
            wallpaper_name = wallpaper_name[0].text
        wallpaper = helper.append_data(wallpaper_name, wall_uuid)

    res = {'Input': wallpaper}

    # Get the information to change the wallpaper
    information = helper.extract_value_from_string_or_dict(elem, 'WFInput')
    if information is None:
        information = ''
    res['Set To'] = information

    # Get the type to change the wallpaper
    location_elem = helper.get_elements_after_key(elem, 'WFWallpaperLocation', 'array')
    if location_elem is not None:
        if len(location_elem[0]) == 0:
            res['Location'] = ''
        else:
            res['Location'] = location_elem[0][0].text
    else:
        # Get to dict or string
        location_elem = helper.extract_value_from_string_or_dict(elem, 'WFWallpaperLocation')
        if location_elem is None:
            res['Location'] = 'Lock Screen and Home Screen'
        else:
            res['Location'] = location_elem

    # Get Show preview if no input for the wallpaper
    if wallpaper == '':
        show_preview = True
        show_preview_elem = helper.get_elements_after_key(elem, 'WFWallpaperShowPreview', 'false')
        if show_preview_elem is not None:
            show_preview = False
        res['Show Preview'] = show_preview

    # Get the Crop to Fit
    crop_to_fit = True
    crop_to_fit_elem = helper.get_elements_after_key(elem, 'WFWallpaperSmartCrop', 'false')
    if crop_to_fit_elem is not None:
        crop_to_fit = False
    res['Crop to Subject'] = crop_to_fit

    # Get the Legibility Blur
    legibility_blur = True
    legibility_blur_elem = helper.get_elements_after_key(elem, 'WFWallpaperLegibilityBlur', 'false')
    if legibility_blur_elem is not None:
        legibility_blur = False
    res['Legibility Blur'] = legibility_blur

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name
    return helper.append_data(res, uuid)
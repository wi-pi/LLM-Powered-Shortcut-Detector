import parse_xml.parse_shortcut_WF as helper


def action_posters_switch(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Wallpaper': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get custom output name if have
    custom_output_name = helper.get_elements_after_key(elem, 'CustomOutputName', 'string')
    if custom_output_name is not None:
        custom_output_name = custom_output_name[0].text

    # Get the poster
    wallpaper = ''
    poster = helper.get_elements_after_key(elem, 'WFPoster', 'dict')
    if poster is not None:
        if poster[0][0].tag == 'key' and poster[0][0].text == 'Value':
            temp_elem = poster[0][1]
            wallpaper = helper.get_attachments_by_range(temp_elem)
        else:
            wall_uuid = helper.track_uuid(poster[0])
            if wall_uuid is None:
                raise ValueError('Invalid Set Wallpaper action')
            wallpaper_name = helper.get_elements_after_key(poster[0], 'name', 'string')
            if wallpaper_name is None:
                raise ValueError('Invalid Set Wallpaper action')
            wallpaper_name = wallpaper_name[0].text
            wallpaper = helper.append_data(wallpaper_name, wall_uuid)

    res = {'Wallpaper': wallpaper}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
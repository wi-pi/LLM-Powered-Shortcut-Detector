import parse_xml.parse_shortcut_WF as helper


def action_giphy(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Find': '', 'GIFs on Giphy': '', 'Show GIF Picker': True, 'Select Multiple': False}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.track_custom_name(elem)

    # Get the input
    input_text = helper.extract_value_from_string_or_dict(elem, 'WFGiphyQuery')
    if input_text is None:
        input_text = ''

    # Get the show gif picker
    show_gif_picker = helper.get_elements_after_key(elem, 'WFGiphyShowPicker', 'false')
    if show_gif_picker is not None:
        show_gif_picker = False
    else:
        show_gif_picker = True

    res = {'Find': input_text, 'GIFs on Giphy': '', 'Show GIF Picker': show_gif_picker}

    # Get the select multiple if picker is shown
    if show_gif_picker:
        select_multiple = helper.get_elements_after_key(elem, 'WFGiphySelectMultiple', 'true')
        if select_multiple is not None:
            select_multiple = True
        else:
            select_multiple = False
        res['Select Multiple'] = select_multiple
    else:
        # Get the number of gifs to select if picker is not shown
        num_to_get = helper.get_elements_after_key(elem, 'WFGiphyLimit', 'real')
        if num_to_get is not None:
            num_to_get = int(num_to_get[0].text)
        else:
            num_to_get = 1
        res['Get # of GIFs'] = num_to_get

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
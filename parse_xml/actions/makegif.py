import parse_xml.parse_shortcut_WF as helper


def action_makegif(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Make GIF from': '', 'Seconds Per Photo': '0.2', 'Loop Forever': True, 'Auto Size': True}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.track_custom_name(elem)

    # Get the input
    input_text = helper.extract_value_from_string_or_dict(elem, 'WFInput')
    if input_text is None:
        input_text = ''

    res = {'Make GIF from': input_text}

    # Get the seconds per photo
    seconds_per_photo = helper.extract_value_from_string_or_dict(elem, 'WFMakeGIFActionDelayTime')
    if seconds_per_photo is None:
        seconds_per_photo = '0.2'

    res['Seconds Per Photo'] = seconds_per_photo

    # Get the loop forever
    loop_forever = helper.get_elements_after_key(elem, 'WFMakeGIFActionLoopEnabled', 'false')
    if loop_forever is not None:
        loop_forever = False
    else:
        loop_forever = True

    res['Loop Forever'] = loop_forever

    # if the loop forever is false, get the loop count
    if not loop_forever:
        loop_count = helper.extract_value_from_string_or_dict(elem, 'WFMakeGIFActionLoopCount')
        if loop_count is None:
            loop_count = 1
        res['Loop Count'] = loop_count

    # Get the auto size
    auto_size = helper.get_elements_after_key(elem, 'WFMakeGIFActionAutoSize', 'false')
    if auto_size is not None:
        auto_size = False
    else:
        auto_size = True

    res['Auto Size'] = auto_size

    # Get the size if auto size is false
    if not auto_size:
        width = helper.extract_value_from_string_or_dict(elem, 'WFMakeGIFActionManualSizeWidth')
        if width is None:
            width = '500'
        res['Width'] = width

        height = helper.extract_value_from_string_or_dict(elem, 'WFMakeGIFActionManualSizeHeight')
        if height is None:
            height = '500'
        res['Height'] = height

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
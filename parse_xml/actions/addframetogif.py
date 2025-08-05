import parse_xml.parse_shortcut_WF as helper


def action_addframetogif(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Add': '', 'to': '', 'Delay Time': '0.25', 'Auto Size': True}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.track_custom_name(elem)

    # Get the input
    input_text = helper.extract_value_from_string_or_dict(elem, 'WFImage')
    if input_text is None:
        input_text = ''

    # Get the to
    to = helper.extract_value_from_string_or_dict(elem, 'WFInputGIF')
    if to is None:
        to = ''

    res = {'Add': input_text, 'to': to}

    # Get the delay time
    delay_time = helper.extract_value_from_string_or_dict(elem, 'WFGIFDelayTime')
    if delay_time is None:
        delay_time = '0.25'

    res['Delay Time'] = delay_time

    # Get the auto size
    auto_size = helper.get_elements_after_key(elem, 'WFGIFAutoSize', 'false')
    if auto_size is not None:
        auto_size = False
    else:
        auto_size = True

    res['Auto Size'] = auto_size

    # if auto size is false, get the width and height
    if not auto_size:
        width = helper.extract_value_from_string_or_dict(elem, 'WFGIFManualSizeWidth')
        if width is None:
            width = '500'
        res['Width'] = width

        height = helper.extract_value_from_string_or_dict(elem, 'WFGIFManualSizeHeight')
        if height is None:
            height = '500'
        res['Height'] = height

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
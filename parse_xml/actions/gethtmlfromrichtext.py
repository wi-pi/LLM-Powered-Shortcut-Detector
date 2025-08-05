import parse_xml.parse_shortcut_WF as helper


def action_gethtmlfromrichtext(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Make HTML from': '', 'Make Full Document': False}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.track_custom_name(elem)

    # Get the input
    input_text = helper.extract_value_from_string_or_dict(elem, 'WFInput')
    if input_text is None:
        input_text = ''

    # Get the make full document
    make_full_document = helper.get_elements_after_key(elem, 'WFMakeFullDocument', 'true')
    if make_full_document is not None:
        make_full_document = True
    else:
        make_full_document = False

    res = {'Make HTML from': input_text, 'Make Full Document': make_full_document}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
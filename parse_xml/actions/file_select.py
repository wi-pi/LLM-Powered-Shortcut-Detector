import parse_xml.parse_shortcut_WF as helper


def action_file_select(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Select': '', 'Select Multiple': False}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output name if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the from input
    from_input = helper.extract_value_from_string_or_dict(elem, 'WFPickingMode')
    if from_input is None:
        from_input = ''

    # Get the select multiple
    select_multiple = helper.get_elements_after_key(elem, 'SelectMultiple', 'true')
    if select_multiple is not None:
        select_multiple = True
    else:
        select_multiple = False

    res = {'Select': from_input, 'Select Multiple': select_multiple}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
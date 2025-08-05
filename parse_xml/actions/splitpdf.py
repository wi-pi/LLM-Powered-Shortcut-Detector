import parse_xml.parse_shortcut_WF as helper


def action_splitpdf(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Split PDF': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output name if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the split input
    split_input = helper.get_elements_after_key(elem, 'WFInput', 'dict')
    if split_input is not None:
        split_input = helper.parse_file_input(split_input[0], 'WFInput')
    if split_input is None:
        split_input = ''

    res = {'Split PDF': split_input}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
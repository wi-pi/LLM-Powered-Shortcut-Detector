import parse_xml.parse_shortcut_WF as helper


def action_compresspdf(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Optimize file size of': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output name if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the from input
    from_input = helper.get_elements_after_key(elem, 'WFInput', 'dict')
    if from_input is not None:
        from_input = helper.parse_file_input(from_input[0], 'WFInput')
    if from_input is None:
        from_input = ''

    res = {'Optimize file size of': from_input}
    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
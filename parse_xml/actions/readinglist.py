import parse_xml.parse_shortcut_WF as helper


def action_readinglist(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Add': '', 'to Reading List': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.track_custom_name(elem)

    # Get the input
    input_text = helper.get_elements_after_key(elem, 'WFURL', 'array')
    if input_text is None:
        input_text = helper.extract_value_from_string_or_dict(elem, 'WFURL')
    else:
        link_list = []
        for item in input_text[0]:
            item = helper.get_final_value(item)
            link_list.append(helper.get_attachments_by_range(item))
        input_text = link_list
    if input_text is None:
        input_text = ''

    res = {'Add': input_text, 'to Reading List': ''}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
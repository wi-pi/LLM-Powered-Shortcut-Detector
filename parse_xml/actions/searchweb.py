import parse_xml.parse_shortcut_WF as helper


def action_searchweb(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Search': '', 'for': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.track_custom_name(elem)

    # Get the searching tool
    search_tool = helper.extract_value_from_string_or_dict(elem, 'WFSearchWebDestination')
    if search_tool is None:
        search_tool = 'Google'

    # Get the input
    input_text = helper.extract_value_from_string_or_dict(elem, 'WFInputText')
    if input_text is None:
        input_text = ''

    res = {'Search': search_tool, 'for': input_text}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
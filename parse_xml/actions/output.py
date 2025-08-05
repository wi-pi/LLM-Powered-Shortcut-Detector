import parse_xml.parse_shortcut_WF as helper


def action_output(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Stop and Output': '', 'Nowhere Behavior': 'Do Nothing'}, None)

    # Track the UUID
    uuid = helper.track_uuid(elem)

    # Find the custom output name
    custom_output_name = helper.track_custom_name(elem)

    # Get the output content, should be string or dict after WFOutput
    output_content = helper.extract_value_from_string_or_dict(elem, 'WFOutput')
    if output_content is None:
        output_content = ''

    res = {'Stop and Output': output_content}

    # Get the nowhere to output action
    action = 'Do Nothing'
    action_nowhere = helper.get_elements_after_key(elem, 'WFNoOutputSurfaceBehavior', 'string')
    if action_nowhere is not None:
        action = action_nowhere[0].text
    res['Nowhere Behavior'] = action

    if action == 'Respond':
        # Get content to respond
        respond_content = helper.extract_value_from_string_or_dict(elem, 'WFResponse')
        if respond_content is None:
            respond_content = ''
        res['Respond Content'] = respond_content

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
import parse_xml.parse_shortcut_WF as helper


def action_openworkflow(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Open Shortcut': ''}, None)

    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.track_custom_name(elem)

    # Get the workflow to run
    workflow = helper.extract_value_from_string_or_dict(elem, 'WFWorkflowName')
    if workflow is None:
        workflow = ''

    res = {
        'Open Shortcut': workflow,
    }

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
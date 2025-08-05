import parse_xml.parse_shortcut_WF as helper


def action_openapp(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Open': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.get_elements_after_key(elem, 'CustomOutputName', 'string')
    if custom_output_name is not None:
        custom_output_name = custom_output_name[0].text

    # Get the app identifier
    app_identifier = helper.get_elements_after_key(elem, 'WFAppIdentifier', 'string')
    app_identifier = '' if app_identifier is None else app_identifier[0].text

    # Get the app name
    app_name = ''
    app_dict = helper.get_elements_after_key(elem, 'WFSelectedApp', 'dict')
    if app_dict is not None:
        app_name = helper.get_elements_after_key(app_dict[0], 'Name', 'string')
        app_name = '' if app_name is None else app_name[0].text

    if app_name == '' and app_dict is not None:
        # Might be an attachment
        app_dict = helper.get_final_value(app_dict[0])
        if app_dict is not None:
            app_name = helper.get_attachments_by_range(app_dict)

    res = {'Open': {'Identifier': app_identifier, 'Name': app_name}}
    if custom_output_name is not None:
        res['Custom Output Name'] = custom_output_name
    return helper.append_data(res, uuid)

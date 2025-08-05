import parse_xml.parse_shortcut_WF as helper


def action_runextension(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Share': '', 'with': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output name if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the share input
    share_input = helper.extract_value_from_string_or_dict(elem, 'WFInput')
    if share_input is None:
        share_input = ''

    # Get the with input app
    app_name = ''
    app_elem = helper.get_elements_after_key(elem, 'WFApp', 'dict')
    if app_elem is not None:
        name_elem = helper.get_elements_after_key(app_elem[0], 'Name', 'string')
        if name_elem is not None:
            app_name = helper.extract_value(name_elem[0])
            if app_name == '':
                raise ValueError('Invalid Run Extension action')

    res = {'Share': share_input, 'with': app_name}
    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)


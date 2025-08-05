import parse_xml.parse_shortcut_WF as helper


def action_openin(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Open': '', 'in': '', 'Show Open In Menu': False}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output name if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the from input
    from_input = ''
    parse_elem = helper.get_elements_after_key(elem, 'WFInput', 'dict')
    if parse_elem is not None:
        from_input = helper.parse_file_input(parse_elem[0], 'WFInput')
    if from_input is None:
        from_input = ''

    # Get the in input
    app = helper.get_elements_after_key(elem, 'WFSelectedApp', 'dict')
    if app is not None:
        app = helper.parse_app_input(app[0])
        if app is None:
            app = helper.extract_value_from_string_or_dict(elem, 'WFSelectedApp')
    else:
        app = ''

    # Get the show open in menu
    show_open_in_menu = helper.get_elements_after_key(elem, 'WFOpenInAskWhenRun', 'true')
    if show_open_in_menu is not None:
        show_open_in_menu = True
    else:
        show_open_in_menu = False

    res = {}
    if show_open_in_menu:
        res = {'Open': from_input, 'Show Open In Menu': show_open_in_menu}
    else:
        res = {'Open': from_input, 'in': app, 'Show Open In Menu': show_open_in_menu}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
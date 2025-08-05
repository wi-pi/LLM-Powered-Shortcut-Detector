import parse_xml.parse_shortcut_WF as helper


def action_showwebpage(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Show web view at': '', 'Enter Safari Reader': False}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.track_custom_name(elem)

    # Get the URL
    url = helper.extract_value_from_string_or_dict(elem, 'WFURL')
    if url is None:
        url = ''

    # Get the show reader
    show_reader = helper.get_elements_after_key(elem, 'WFEnterSafariReader', 'true')
    if show_reader is not None:
        show_reader = True
    else:
        show_reader = False

    res = {'Show web view at': url, 'Enter Safari Reader': show_reader}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
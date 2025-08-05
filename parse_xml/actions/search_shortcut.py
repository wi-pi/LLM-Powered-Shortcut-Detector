import parse_xml.parse_shortcut_WF as helper


def action_search_shortcut(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Search in Shortcuts': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    search_query = helper.extract_value_from_string_or_dict(elem, 'searchPhrase')
    if search_query is None:
        search_query = ''

    res = {'Search in Shortcuts': search_query}


    if custom_output_name is not None:
        res['Output Name'] = custom_output_name
    return helper.append_data(res, uuid)
import parse_xml.parse_shortcut_WF as helper


def action_search_inreminder(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Search': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # Get what to search
    search = helper.extract_value_from_string_or_dict(elem, 'searchPhrase')
    if search is None:
        search = ''

    res = {'Search': search}


    if custom_output_name is not None:
        res['Output Name'] = custom_output_name
    return helper.append_data(res, uuid)
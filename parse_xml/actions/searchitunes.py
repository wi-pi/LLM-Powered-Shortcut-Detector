import parse_xml.parse_shortcut_WF as helper


def action_searchitunes(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Find in iTunes Store': '', 'Media Type': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    term = helper.extract_value_from_string_or_dict(elem, 'WFSearchTerm')
    if term is None:
        term = ''

    media = helper.extract_value_from_string_or_dict(elem, 'WFMediaType')
    if media is None:
        media = ''

    res = {'Find in iTunes Store': term, 'Media Type': media}


    if custom_output_name is not None:
        res['Output Name'] = custom_output_name
    return helper.append_data(res, uuid)
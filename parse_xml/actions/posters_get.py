import parse_xml.parse_shortcut_WF as helper


def action_posters_get(elem):
    if not helper.check_validation(elem):
        raise ValueError('Invalid Get Posters action')

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.get_elements_after_key(elem, 'CustomOutputName', 'string')
    if custom_output_name is not None:
        custom_output_name = custom_output_name[0].text

    # Get the option to get the posters
    poster_type = helper.extract_value_from_string_or_dict(elem, 'WFPosterType')
    if poster_type is None:
        poster_type = 'All'

    res = {'Type': poster_type}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name
    return helper.append_data(res, uuid)
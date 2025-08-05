import parse_xml.parse_shortcut_WF as helper
from parse_xml_output.parse_output_to_natural_language import parse_get_attachment


def action_search_message_mail(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Search': ' in Mail'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output name if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the search term
    search_term = helper.extract_value_from_string_or_dict(elem, 'searchPhrase')
    if search_term is None:
        search_term = ' in Mail'
    else:
        if type(search_term) == list:
            search_term = parse_get_attachment(search_term)

        search_term = f"{search_term} in Mail"

    res = {'Search': search_term}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
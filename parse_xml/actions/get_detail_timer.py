import parse_xml.parse_shortcut_WF as helper
import parse_xml_output.parse_output_to_natural_language as parse_output



def action_get_detail_timer(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Get': 'Remaining Time of the Current Timer'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output name if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the get type input
    get_type = helper.extract_value_from_string_or_dict(elem, 'mode')
    if get_type is None:
        get_type = 'Remaining Time of the Current Timer'
    else:
        if type(get_type) == list:
            get_type = parse_output.parse_get_attachment(get_type)
        get_type = f"{get_type} of the Current Timer"

    res = {'Get': get_type}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
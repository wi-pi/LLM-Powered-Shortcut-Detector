import parse_xml.parse_shortcut_WF as helper


def action_getcurrentlocation(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Precision': 'Nearest Hundred Meters'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output name if have
    custom_output_name = helper.get_elements_after_key(elem, 'CustomOutputName', 'string')
    if custom_output_name is not None:
        custom_output_name = custom_output_name[0].text

    # Get the location accuracy
    location = helper.extract_value_from_string_or_dict(elem, 'Accuracy')
    if location is None:
        location = 'Nearest Hundred Meters'

    res = {'Precision': location}

    return helper.append_data(res, uuid)
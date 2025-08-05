import parse_xml.parse_shortcut_WF as helper


def action_date(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Date Mode': 'Current Date'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    res = {}

    # Find if the element have custom output name
    custom_output_name = helper.track_custom_name(elem)

    # Get the date mode under WFDateActionMode, string or dict
    date_elem = helper.extract_value_from_string_or_dict(elem, 'WFDateActionMode')
    if date_elem is None:
        date_elem = 'Current Date'

    res['Date Mode'] = date_elem

    # Get the date data if specified date
    if date_elem == 'Specified Date':
        date_data = helper.extract_value_from_string_or_dict(elem, 'WFDateActionDate')
        if date_data is None:
            # Date of IPhone release
            date_data = 'June 29, 2007'
        res['Date Data'] = date_data

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
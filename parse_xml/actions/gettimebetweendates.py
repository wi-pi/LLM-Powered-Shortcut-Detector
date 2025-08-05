import parse_xml.parse_shortcut_WF as helper


def action_gettimebetweendates(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Starting Time': '', 'Ending Time': '', 'Unit': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    res = {}

    # Find if the element have custom output name
    custom_output_name = helper.get_elements_after_key(elem, 'CustomOutputName', 'string')
    if custom_output_name is not None:
        custom_output_name = custom_output_name[0].text

    # Get the starting time (A)-- WFTimeUntilFromDate
    starting_time = helper.extract_value_from_string_or_dict(elem, 'WFTimeUntilFromDate')
    if starting_time is None:
        res['Starting Time'] = ''
    else:
        res['Starting Time'] = starting_time

    # Get the ending time (B)-- WFInput
    ending_time = helper.extract_value_from_string_or_dict(elem, 'WFInput')
    if ending_time is None:
        res['Ending Time'] = ''
    else:
        res['Ending Time'] = ending_time

    # Get the unit format
    unit_elem = helper.extract_value_from_string_or_dict(elem, 'WFTimeUntilUnit')
    if unit_elem is None:
        unit_elem = 'Minutes'

    res['Unit'] = unit_elem

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)


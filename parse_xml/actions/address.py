import parse_xml.parse_shortcut_WF as helper


def action_address(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Line 1': '', 'Line 2': '', 'City': '', 'State': '', 'Postal Code': '', 'Region': ''},None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output name if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the address
    address_line1 = helper.extract_value_from_string_or_dict(elem, 'WFAddressLine1')
    if address_line1 is None:
        address_line1 = ''
    address_line2 = helper.extract_value_from_string_or_dict(elem, 'WFAddressLine2')
    if address_line2 is None:
        address_line2 = ''
    city = helper.extract_value_from_string_or_dict(elem, 'WFCity')
    if city is None:
        city = ''
    state = helper.extract_value_from_string_or_dict(elem, 'WFState')
    if state is None:
        state = ''
    postal_code = helper.extract_value_from_string_or_dict(elem, 'WFPostalCode')
    if postal_code is None:
        postal_code = ''
    country = helper.extract_value_from_string_or_dict(elem, 'WFCountry')
    if country is None:
        country = 'United States'

    res = {'Line 1': address_line1, 'Line 2': address_line2, 'City': city, 'State': state, 'Postal Code': postal_code, 'Region': country}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
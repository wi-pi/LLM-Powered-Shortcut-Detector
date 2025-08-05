import parse_xml.parse_shortcut_WF as helper


def action_getipaddress(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Address': 'External', 'Address Type': 'IPv4'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.get_elements_after_key(elem, 'CustomOutputName', 'string')
    if custom_output_name is not None:
        custom_output_name = custom_output_name[0].text

    # Check if it ask for other address
    address = helper.extract_value_from_string_or_dict(elem, 'WFIPAddressSourceOption')
    if address is None:
        address = 'External'

    res = {'Address': address}

    # Check type of address
    address_type = helper.extract_value_from_string_or_dict(elem, 'WFIPAddressTypeOption')
    if address_type is None:
        address_type = 'IPv4'

    res['Address Type'] = address_type

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
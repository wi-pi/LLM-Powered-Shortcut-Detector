import parse_xml.parse_shortcut_WF as helper


def action_health_quantity_log(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Log Health Quantity': '', 'Type': '', 'Date': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the type
    type = helper.extract_value_from_string_or_dict(elem, 'WFQuantitySampleType')
    if type is None:
        type = ''

    res = {'Log Health Quantity': '', 'Type': type}

    # Get the value if have type
    if type != '':
        value = helper.get_elements_after_key(elem, 'WFQuantitySampleQuantity', 'dict')
        if value is None:
            value = ''
        else:
            value_elem = helper.get_final_value(value[0])
            value = helper.extract_value_from_string_or_dict(value_elem, 'Magnitude')
            unit = helper.extract_value_from_string_or_dict(value_elem, 'Unit')
            value = f"{value} {unit}"

            res['Value'] = value

    # Get the date
    date = helper.extract_value_from_string_or_dict(elem, 'WFQuantitySampleDate')
    if date is None:
        date = ''

    res['Date'] = date

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
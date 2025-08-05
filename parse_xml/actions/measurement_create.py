import parse_xml.parse_shortcut_WF as helper

unit_map = {
    'Length': 'ft',
    'Volume': 'cup',
    'Temperature': '°F',
    'Speed': 'mi/hr',
    'Pressure': '"Hg',
    'Power': 'watt',
    'Mass': 'lb',
    'Information Storage': 'MB',
    'Illuminance': 'lux',
    'Fuel Efficiency': 'mpg',
    'Frequency': 'Hz',
    'Energy': 'joule',
    'Electric Resistance': 'ohm',
    'Electric Potential Difference': 'volt',
    'Electric Current': 'amp',
    'Electric Charge': 'Ah',
    'Duration': 'min',
    'Dispersion': 'ppm',
    'Concentration Mass': 'g/L',
    'Area': 'ft²',
    'Angle': 'deg',
    'Acceleration': 'g-force'
}


def action_measurement_create(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Unit Type': 'Length', 'Value': '', 'Unit': 'ft'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    res = {}

    # Find if the element have custom output name
    custom_output_name = helper.get_elements_after_key(elem, 'CustomOutputName', 'string')
    if custom_output_name is not None:
        custom_output_name = custom_output_name[0].text

    # Get the measurement Unit Type
    measurement_unit_elem = helper.extract_value_from_string_or_dict(elem, 'WFMeasurementUnitType')
    if measurement_unit_elem is None:
        measurement_unit_elem = 'Length'

    res['Unit Type'] = measurement_unit_elem

    input = ''
    unit_val = ''
    # Get the measurement Unit and val
    input_val_unit_elem = helper.get_elements_after_key(elem, 'WFMeasurementUnit', 'dict')
    if input_val_unit_elem is not None:
        input_val_unit_elem = helper.get_final_value(input_val_unit_elem[0])
        magnitude_elem = helper.extract_value_from_string_or_dict(input_val_unit_elem, 'Magnitude')
        if magnitude_elem is None:
            input = ''
        unit_elem = helper.get_elements_after_key(input_val_unit_elem, 'Unit', 'string')
        if unit_elem is not None:
            unit_val = unit_elem[0].text
        else:
            if type(measurement_unit_elem) == str and measurement_unit_elem in unit_map:
                unit_val = unit_map[measurement_unit_elem]
            # else:
            #     raise ValueError('No Unit found in Measurement Create action')
    else:
        if measurement_unit_elem == 'Length':
            input = ''
            unit_val = 'ft'

    res['Unit'] = unit_val
    res['Value'] = input

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
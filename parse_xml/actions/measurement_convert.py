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

def action_measurement_convert(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'From Input': '', 'To Unit Type': 'Length', 'To Unit': 'feet'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    res = {}

    # Find if the element have custom output name
    custom_output_name = helper.track_custom_name(elem)

    input = ''
    # Get the measurement from input
    input_elem = helper.get_elements_after_key(elem, 'WFInput', 'dict')
    if input_elem is not None:
        input_elem = helper.get_final_value(input_elem[0])
        input = helper.get_attachments_by_range(input_elem)

    res['From Input'] = input

    # Get the measurement Unit Type -- string or dict
    from_measurement_unit_elem = helper.extract_value_from_string_or_dict(elem, 'WFMeasurementUnitType')
    if from_measurement_unit_elem is None:
        from_measurement_unit_elem = 'Length'

    res['To Unit Type'] = from_measurement_unit_elem

    # Get the measurement Unit
    unit_elem = helper.extract_value_from_string_or_dict(elem, 'WFMeasurementUnit')
    if unit_elem is None:
        if type(from_measurement_unit_elem) == str and from_measurement_unit_elem in unit_map:
            unit_elem = unit_map[from_measurement_unit_elem]
        else:
            if from_measurement_unit_elem == 'Length':
                unit_elem = 'feet'
            else:
                unit_elem = ''

    res['To Unit'] = unit_elem

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
import parse_xml.parse_shortcut_WF as helper


def action_adjustdate(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Operation': 'Add', 'Input': '', 'Amount': '0', 'Unit': 'seconds'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    res = {}

    # Find if the element have custom output name
    custom_output_name = helper.track_custom_name(elem)

    # Get the adjustment operation - could be a string after WFAdjustOperation
    adjustment_elem = helper.get_elements_after_key(elem, 'WFAdjustOperation', 'string')
    if adjustment_elem is not None:
        adjustment_elem = adjustment_elem[0].text
    else:
        adjustment_elem = 'Add'

    res['Operation'] = adjustment_elem

    # Get the duration: both value and unit -- a dict after WFDuration that contains both
    if adjustment_elem == 'Add' or adjustment_elem == 'Subtract':
        duration_elem = helper.get_elements_after_key(elem, 'WFDuration', 'dict')
        magnitude_elem = '0'
        unit_elem = 'seconds'
        if duration_elem is not None:
            # Find magnitude
            duration_elem = helper.get_final_value(duration_elem[0])
            magnitude_elem = helper.extract_value_from_string_or_dict(duration_elem, 'Magnitude')
            if magnitude_elem is None:
                magnitude_elem = '0'



            # Find unit
            unit_elem = helper.get_elements_after_key(duration_elem, 'Unit', 'string')
            if unit_elem is not None:
                unit_elem = unit_elem[0].text
            else:
                unit_elem = 'seconds'

        res['Amount'] = magnitude_elem
        res['Unit'] = unit_elem


    # Get the value of adjustment - could be a string or a dict after WFAdjustDateValue
    value_elem = helper.extract_value_from_string_or_dict(elem, 'WFDate')
    if value_elem is None:
        value_elem = ''

    res['Input'] = value_elem

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
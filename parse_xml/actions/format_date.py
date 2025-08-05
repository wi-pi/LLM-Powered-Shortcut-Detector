import parse_xml.parse_shortcut_WF as helper


def action_format_date(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Input': '', 'Date Format': 'Short', 'Time Format': 'Short', 'Locale': 'Default'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.get_elements_after_key(elem, 'CustomOutputName', 'string')
    if custom_output_name is not None:
        custom_output_name = custom_output_name[0].text

    res = {}

    # Get the data to format, string or dict after WFDate
    date_elem = helper.extract_value_from_string_or_dict(elem, 'WFDate')
    if date_elem is None:
        date_elem = ''

    res['Input'] = date_elem

    # Get the Date format, default is Short
    date_format_elem = helper.extract_value_from_string_or_dict(elem, 'WFDateFormatStyle')
    if date_format_elem is None:
        date_format_elem = 'Short'

    res['Date Format'] = date_format_elem

    # Get the time format if date format is in ['None', 'Short', 'Long', 'Medium', 'Relative'], could be string or dict
    if date_format_elem in ['None', 'Short', 'Long', 'Medium', 'Relative']:
        time_format_elem = helper.extract_value_from_string_or_dict(elem, 'WFTimeFormatStyle')
        if time_format_elem is None:
            time_format_elem = 'Short'

        if time_format_elem == 'Relative' or time_format_elem == 'Custom':
            res.pop('Date Format')

        res['Time Format'] = time_format_elem

    # Get the Locale if date format is not in ['ISO 8601', 'RFC 2822']
    if date_format_elem not in ['ISO 8601', 'RFC 2822']:
        locale_elem = helper.extract_value_from_string_or_dict(elem, 'WFLocale')
        if locale_elem is None:
            locale_elem = 'Default'

        res['Locale'] = locale_elem

    # Get the Format String if date format is 'Custom'
    if date_format_elem == 'Custom':
        format_string_elem = helper.extract_value_from_string_or_dict(elem, 'WFDateFormat')
        if format_string_elem is None:
            format_string_elem = 'EEE, dd MMM yyyy HH:mm:ss Z'

        res['Format String'] = format_string_elem

    # Ge the alternate format if date format is 'Relative'
    if date_format_elem == 'Relative':
        alternate_format_elem = helper.extract_value_from_string_or_dict(elem, 'WFRelativeDateFormatStyle')
        if alternate_format_elem is None:
            alternate_format_elem = 'Medium'

        res['Alternate Format'] = alternate_format_elem

    # Get the include ISO 8601 Time, true or false, default is false
    if date_format_elem == 'ISO 8601':
        include_elem = helper.get_elements_after_key(elem, 'WFISO8601IncludeTime', 'true')
        if include_elem is not None:
            include_elem = True
        else:
            include_elem = False

        res['Include ISO 8601 Time'] = include_elem




    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
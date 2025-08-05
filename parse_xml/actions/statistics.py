import parse_xml.parse_shortcut_WF as helper


def action_statistics(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Calculate the': 'Average', 'of':''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    res = {}

    # Find if the element have custom output name
    custom_output_name = helper.get_elements_after_key(elem, 'CustomOutputName', 'string')
    if custom_output_name is not None:
        custom_output_name = custom_output_name[0].text

    # Get the statistics operation - could be a string or a dict after WFStatisticsOperation
    statistics_elem = helper.extract_value_from_string_or_dict(elem, 'WFStatisticsOperation')
    if statistics_elem is None:
        statistics_elem = 'Average'

    res['Calculate the'] = statistics_elem

    # Get the input data -- dict after Input
    input_data = ''
    input_data_elem = helper.get_elements_after_key(elem, 'Input', 'dict')
    if input_data_elem is not None:
        input_data = helper.get_final_value(input_data_elem[0])
        input_data = helper.get_attachments_by_range(input_data)

    res['of'] = input_data

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
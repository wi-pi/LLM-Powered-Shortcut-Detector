import parse_xml.parse_shortcut_WF as helper


def action_detect_dictionary(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Get dictionary from': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.track_custom_name(elem)

    res = {}

    # Get the dictionary -- WFInput
    dict_elem = helper.get_elements_after_key(elem, 'WFInput', 'dict')
    if dict_elem is not None:
        dict_elem = helper.get_final_value(dict_elem[0])
        res['Get dictionary from'] = helper.get_attachments_by_range(dict_elem)
    else:
        res['Get dictionary from'] = ''

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name
    return helper.append_data(res, uuid)
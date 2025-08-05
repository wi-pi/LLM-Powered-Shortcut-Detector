# Set value to key in dictionary
import parse_xml.parse_shortcut_WF as helper


def action_setvalueforkey(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Set': '', 'to': '', 'in': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.get_elements_after_key(elem, 'CustomOutputName', 'string')
    if custom_output_name is not None:
        custom_output_name = custom_output_name[0].text

    # Get the key -- WFDictionaryKey
    key = helper.extract_value_from_string_or_dict(elem, 'WFDictionaryKey')
    if key is None:
        key = ''

    # Get the value --WFDictionaryValue
    value = helper.extract_value_from_string_or_dict(elem, 'WFDictionaryValue')
    if value is None:
        value = ''

    # Get the dictionary -- WFDictionary
    dictionary = ''
    dictionary_elem = helper.get_elements_after_key(elem, 'WFDictionary', 'dict')
    if dictionary_elem is not None:
        dictionary_elem = helper.get_final_value(dictionary_elem[0])
        dictionary = helper.get_attachments_by_range(dictionary_elem)

    res = {
        'Set': key,
        'to': value,
        'in': dictionary
    }

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
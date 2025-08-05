import parse_xml.parse_shortcut_WF as helper
import parse_xml.actions.dictionary as dictionary

def action_list(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'List Items': ['One', 'Two']}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.track_custom_name(elem)

    # Get the list items
    list_items = []
    list_items_elem = helper.get_elements_after_key(elem, 'WFItems', 'array')
    if list_items_elem is not None:
        for item in list_items_elem[0]:
            # Could be string or dict
            if item.tag == 'string':
                if item.text is not None:
                    list_items.append(item.text)
                else:
                    list_items.append('')
            elif item.tag == 'dict':
                current_elem = helper.get_elements_after_key(item, 'WFValue', 'dict')
                if current_elem is not None:
                    current_elem = helper.get_final_value(current_elem[0])
                    if current_elem[0].tag == 'key' and current_elem[0].text == 'WFDictionaryFieldValueItems':
                        item_elem = helper.get_elements_after_key(current_elem, 'WFDictionaryFieldValueItems', 'array')
                        if item_elem is not None:
                            for item in item_elem[0]:
                                key_value = dictionary.recursive_dict(item, 'WFKey')
                                value_value = dictionary.recursive_dict(item, 'WFValue')
                                new_dict = {'key': key_value, 'value': value_value}
                                list_items.append(new_dict)
                        else:
                            raise ValueError('No WFDictionaryFieldValueItems found in List Items')
                    else:
                        item_elem = helper.get_final_value(current_elem[0])
                        list_items.append(helper.get_attachments_by_range(item_elem))
                else:
                    raise ValueError('No WFValue found in List Items')
            else:
                raise ValueError('Unknown type found in List Items')
    else:
        list_items = ['One', 'Two']
    res = {'List Items': list_items}
    if custom_output_name is not None:
        res['Output Name'] = custom_output_name
    return helper.append_data(res, uuid)

import parse_xml.parse_shortcut_WF as helper


def action_delay(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Wait': '1 second'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the delay time
    delay_time = '1'
    delay_time_elem = helper.get_elements_after_key(elem, 'WFDelayTime', 'real')
    if delay_time_elem is not None:
        delay_time = delay_time_elem[0].text
    else:
        if helper.get_elements_after_key(elem, 'WFDelayTime', 'dict') is not None:
            delay_time_elem = helper.get_final_value(helper.get_elements_after_key(elem, 'WFDelayTime', 'dict')[0])
            delay_time = helper.get_attachments_by_range(delay_time_elem)
        else:
            if helper.get_elements_after_key(elem, 'WFDelayTime', 'integer') is not None:
                delay_time = helper.get_elements_after_key(elem, 'WFDelayTime', 'integer')[0].text
            else:
                raise ValueError('No WFDelayTime found in Delay action')

    delay_time = helper.list_to_str(delay_time)
    delay_time = f"{delay_time} seconds"

    res = {'Wait': delay_time}

    if helper.track_custom_name(elem):
        res['Custom Name'] = helper.track_custom_name(elem)

    return helper.append_data(res, uuid)

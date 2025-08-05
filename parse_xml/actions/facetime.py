import parse_xml.parse_shortcut_WF as helper
from parse_xml_output.parse_output_to_natural_language import parse_get_attachment


def action_facetime(elem, client_number):
    if not helper.check_validation(elem):
        return helper.append_data({'FaceTime Call': ''}, None)


    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output name if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the action mode
    action_mode = helper.extract_value_from_string_or_dict(elem, 'WFFaceTimeType')
    if action_mode is None:
        action_mode = 'FaceTime Call'
    else:
        if action_mode == 'Audio':
            action_mode = 'FaceTime Audio Call'
        else:
            action_mode = f"{parse_get_attachment(action_mode)} Call"

    # Get the people to call array or dict
    people_to_call_elem = helper.get_elements_after_key(elem, 'WFFaceTimeContact', 'dict')
    if people_to_call_elem is not None:
        people_to_call_elem = helper.parse_contact_info(people_to_call_elem[0], client_number)
    else:
        people_to_call_elem = ''

    res = {action_mode: people_to_call_elem}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)



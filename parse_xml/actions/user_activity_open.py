import parse_xml.parse_shortcut_WF as helper
import base64


def action_user_activity_open(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'User activity for App': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output name if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the user activity
    user_activity = helper.get_elements_after_key(elem, 'UserActivityDescriptor', 'dict')
    if user_activity is not None:
        user_activity = helper.extract_value_from_string_or_dict(user_activity[0], 'Name')
    else:
        user_activity = ''


    res = {'User activity from App': user_activity}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
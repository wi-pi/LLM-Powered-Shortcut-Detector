import parse_xml.parse_shortcut_WF as helper

def action_showresult(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Show': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # The result could either be in string or a dictionary
    # First try string
    result_elem = helper.extract_value_from_string_or_dict(elem, 'Text')
    if result_elem is None:
        result_elem = ''

    res = {'Show': result_elem}

    return helper.append_data(res, uuid)
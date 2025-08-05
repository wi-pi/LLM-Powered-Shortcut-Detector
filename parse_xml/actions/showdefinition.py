import parse_xml.parse_shortcut_WF as helper


def action_showdefinition(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Show definition of': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the definition
    definition = helper.extract_value_from_string_or_dict(elem, 'Word')
    if definition is None:
        definition = ''

    res = {'Show definition of': definition}

    return helper.append_data(res, uuid)
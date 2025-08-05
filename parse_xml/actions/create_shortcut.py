import parse_xml.parse_shortcut_WF as helper


def action_create_shortcut(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Create Shortcut named': '', 'Open When Run': True}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    shortcut_name = helper.extract_value_from_string_or_dict(elem, 'name')
    if shortcut_name is None:
        shortcut_name = ''

    open_when_run = helper.get_elements_after_key(elem, 'OpenWhenRun', 'false')
    if open_when_run is not None:
        open_when_run = False
    else:
        open_when_run = True

    res = {'Create Shortcut named': shortcut_name, 'Open When Run': open_when_run}


    if custom_output_name is not None:
        res['Output Name'] = custom_output_name
    return helper.append_data(res, uuid)
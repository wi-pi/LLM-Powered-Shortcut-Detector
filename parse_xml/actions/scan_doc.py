import parse_xml.parse_shortcut_WF as helper


def action_scan_doc(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Action': 'Scan Document', 'Open When Run': True}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the Open When Run
    open_when_run = helper.get_elements_after_key(elem, 'OpenWhenRun', 'false')
    if open_when_run is None:
        open_when_run = True
    else:
        open_when_run = False

    res = {'Action': 'Scan Document', 'Open When Run': open_when_run}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
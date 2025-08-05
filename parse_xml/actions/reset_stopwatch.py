import parse_xml.parse_shortcut_WF as helper


def action_reset_stopwatch(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Reset the Stopwatch': '', 'Open When Run': True}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output name if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the open when run
    open_when_run = helper.get_elements_after_key(elem, 'OpenWhenRun', 'false')
    if open_when_run is not None:
        open_when_run = False
    else:
        open_when_run = True

    res = {'Reset the Stopwatch': '', 'Open When Run': open_when_run}

    return helper.append_data(res, uuid)
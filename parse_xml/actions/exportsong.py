import parse_xml.parse_shortcut_WF as helper


def action_exportsong(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Select music': '', 'Select Multiple Songs': False}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the select multiple
    select_multiple = helper.get_elements_after_key(elem, 'WFExportSongActionSelectMultiple', 'true')
    if select_multiple is not None:
        select_multiple = True
    else:
        select_multiple = False

    res = {'Select music': '', 'Select Multiple Songs': select_multiple}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
import parse_xml.parse_shortcut_WF as helper


def action_selectcontacts(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Select Multiple': False}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the contacts
    contacts = helper.get_elements_after_key(elem, 'WFSelectMultiple', 'true')
    if contacts is None:
        contacts = False
    else:
        contacts = True

    res = {'Select Multiple': contacts}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name
    return helper.append_data(res, uuid)
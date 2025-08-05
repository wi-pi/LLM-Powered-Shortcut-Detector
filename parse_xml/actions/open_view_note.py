import parse_xml.parse_shortcut_WF as helper


def action_open_view_note(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Open the': ' view'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the view to open
    view = helper.extract_value_from_string_or_dict(elem, 'target')
    if view is None:
        view = ' view'
    else:
        view = helper.list_to_str(view)
        view = f"{view} view"

    res = {'Open the': view}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name
    return helper.append_data(res, uuid)
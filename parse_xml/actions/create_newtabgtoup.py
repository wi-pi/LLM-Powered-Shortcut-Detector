import parse_xml.parse_shortcut_WF as helper


def action_create_new_tab_group(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Create Tab Group': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.track_custom_name(elem)

    # Get the tab group name
    tab_group_name = helper.extract_value_from_string_or_dict(elem, 'name')
    if tab_group_name is None:
        tab_group_name = ''

    res = {'Create Tab Group': tab_group_name}
    if custom_output_name is not None:
        res['Output Name'] = custom_output_name
    return helper.append_data(res, uuid)
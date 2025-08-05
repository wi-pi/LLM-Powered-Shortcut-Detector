import parse_xml.parse_shortcut_WF as helper


def action_reset_cellulardata_statistics(elem):
    if not helper.check_validation(elem):
        raise ValueError('Invalid Reset Cellular Data Statistics action')

    # Check UUID
    uuid = helper.track_uuid(elem)

    return helper.append_data({'Action': 'Reset the cellular data usage statistics'}, uuid)
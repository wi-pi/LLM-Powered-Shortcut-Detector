import parse_xml.parse_shortcut_WF as helper


def action_returntohomescreen(elem):
    if helper.check_validation(elem):
        raise ValueError('Invalid return to home screen action')

    return helper.append_data('Go to Home Screen', None)
import parse_xml.parse_shortcut_WF as helper
from parse_xml.actions.output import action_output


def action_exit(elem, client_number):
    if helper.check_validation(elem):
        if client_number <= 900:
            return action_output(elem)
    return helper.append_data('Stop this shortcut', None)
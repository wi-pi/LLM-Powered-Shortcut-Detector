import parse_xml.parse_shortcut_WF as helper


def action_waittoreturn(elem):
    if helper.check_validation(elem):
        raise ValueError('Invalid Wait to Return action.')

    uuid = helper.track_uuid(elem)

    output_name = helper.track_custom_name(elem)

    res = {'Action': 'Wait to Return'}

    if output_name is not None:
        res['Output Name'] = output_name

    return helper.append_data(res, uuid)
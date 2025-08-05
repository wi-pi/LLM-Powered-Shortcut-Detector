import parse_xml.parse_shortcut_WF as helper


def action_setairdroppreceiving(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'State': 'Everyone for 10 Minutes'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    if uuid is not None:
        raise ValueError('UUID is not None for airdrop receiving set')

    output_name = helper.track_custom_name(elem)

    # Get the state
    state = helper.extract_value_from_string_or_dict(elem, 'WFAirDropState')
    if state is None:
        state = 'Everyone for 10 Minutes'

    res = {'State': state}

    if output_name is not None:
        res['Output Name'] = output_name

    return helper.append_data(res, None)
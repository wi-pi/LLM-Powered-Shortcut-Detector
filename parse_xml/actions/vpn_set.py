import parse_xml.parse_shortcut_WF as helper


def action_vpn_set(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Action': 'Connect', 'VPN': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    output_name = helper.track_custom_name(elem)

    # Ge the action
    action = helper.extract_value_from_string_or_dict(elem, 'WFVPNOperation')
    if action is None:
        action = 'Connect'
    res = {'Action': action}

    # Get the VPN
    app_name = ''
    vpn_elem = helper.get_elements_after_key(elem, 'WFVPN', 'dict')
    if vpn_elem is not None:
        # if the vpn is from an app
        vpn_elem = vpn_elem[0]
        if vpn_elem[0].tag == 'key' and vpn_elem[0].text == 'appDescriptor':
            # Get the app name
            app_name = helper.get_elements_after_key(vpn_elem, 'title', 'string')
            if app_name is not None:
                app_name = app_name[0].text
            else:
                raise ValueError('App name not found for VPN')
        else:
            vpn_elem = helper.get_final_value(vpn_elem)
            app_name = helper.get_attachments_by_range(vpn_elem)

    res['VPN'] = app_name

    # If action is Set On Demand, get the state
    if action == 'Set On Demand':
        on_demand = helper.get_elements_after_key(elem, 'WFOnDemandValue', 'integer')
        if on_demand is not None:
            if on_demand[0].text == '1':
                on_demand = 'On'
            else:
                on_demand = 'Off'
            res['On Demand'] = on_demand
        # else:
        #     raise ValueError('On Demand value not found for VPN')

    if output_name is not None:
        res['Output Name'] = output_name

    return helper.append_data(res, uuid)
import parse_xml.parse_shortcut_WF as helper


def action_runsshscript(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Script': ''}, None)

    # Track the UUID
    uuid = helper.track_uuid(elem)

    # Find the custom output name
    custom_output_name = helper.track_custom_name(elem)

    # Find the ssh script
    ssh_script = helper.extract_value_from_string_or_dict(elem, 'WFSSHScript')
    if ssh_script is None:
        ssh_script = ''
    res = {'Script': ssh_script}

    # Find the ssh host
    ssh_host = helper.extract_value_from_string_or_dict(elem, 'WFSSHHost')
    if ssh_host is None:
        ssh_host = '192.168.1.100'
    res['Host'] = ssh_host

    # Find the ssh port
    ssh_port = helper.extract_value_from_string_or_dict(elem, 'WFSSHPort')
    if ssh_port is None:
        ssh_port = '22'
    res['Port'] = ssh_port

    # Find the ssh user
    ssh_user = helper.extract_value_from_string_or_dict(elem, 'WFSSHUser')
    if ssh_user is None:
        ssh_user = 'root'
    res['User'] = ssh_user

    # Find the ssh authentication method
    ssh_auth = helper.get_elements_after_key(elem, 'WFSSHAuthenticationType', 'string')
    if ssh_auth is None:
        ssh_auth = 'Password'
    else:
        ssh_auth = ssh_auth[0].text
    res['Authentication Method'] = ssh_auth

    # Find the ssh password or key
    if ssh_auth == 'Password':
        ssh_password = helper.extract_value_from_string_or_dict(elem, 'WFSSHPassword')
        if ssh_password is None:
            ssh_password = ''
        res['Password'] = ssh_password
    elif ssh_auth == 'SSH Key':
        # Omitted
        pass
    else:
        raise ValueError('Invalid SSH authentication method.')

    # Find the input
    input_ssh = helper.get_elements_after_key(elem, 'WFInput', 'dict')
    if input_ssh is not None:
        input_ssh = helper.get_final_value(input_ssh[0])
        input_ssh = helper.get_attachments_by_range(input_ssh)
    else:
        input_ssh = ''
    res['Input'] = input_ssh


    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
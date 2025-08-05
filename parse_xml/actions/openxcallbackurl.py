import parse_xml.parse_shortcut_WF as helper


def action_openxcallbackurl(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'URL': '', 'Custom Callback': False, 'Custom Success URL': False}, None)

    # Track the UUID
    uuid = helper.track_uuid(elem)

    # Get custom output name if have
    custom_output_name = helper.track_custom_name(elem)

    # Find the input URL
    input_url = helper.extract_value_from_string_or_dict(elem, 'WFXCallbackURL')
    if input_url is None:
        input_url = ''

    res = {'URL': input_url}

    # Get if it allow custom callback
    allow_custom = helper.get_elements_after_key(elem, 'WFXCallbackCustomCallbackEnabled', 'true')
    if allow_custom is not None:
        allow_custom = True
    else:
        allow_custom = False

    res['Custom Callback'] = allow_custom

    # Get if allow custom x-success url
    allow_xsuccess = helper.get_elements_after_key(elem, 'WFXCallbackCustomSuccessURLEnabled', 'true')
    if allow_xsuccess is not None:
        allow_xsuccess = True
    else:
        allow_xsuccess = False

    res['Custom Success URL'] = allow_xsuccess

    # If the allow custom callback is true
    if allow_custom:
        # 1, get the success key
        success_key = helper.extract_value_from_string_or_dict(elem, 'WFXCallbackCustomSuccessKey')
        if success_key is None:
            success_key = 'x-success'
        res['Success Key'] = success_key
        # 2, get the cancel key
        cancel_key = helper.extract_value_from_string_or_dict(elem, 'WFXCallbackCustomCancelKey')
        if cancel_key is None:
            cancel_key = ''
        res['Cancel Key'] = cancel_key
        # 3, get the error key
        error_key = helper.extract_value_from_string_or_dict(elem, 'WFXCallbackCustomErrorKey')
        if error_key is None:
            error_key = ''
        res['Error Key'] = error_key

    if allow_xsuccess:
        xsuccess_url = helper.extract_value_from_string_or_dict(elem, 'WFXCallbackCustomSuccessURL')
        if xsuccess_url is None:
            xsuccess_url = 'shortcuts://callback'
        else:
            if len(xsuccess_url) == 0:
                xsuccess_url = ''
        res['Success URL'] = xsuccess_url

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
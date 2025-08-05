import parse_xml.parse_shortcut_WF as helper

def action_set_voice_data_mode(elem):
    # Validate the input structure
    if not helper.check_validation(elem):
        return helper.append_data({'SetVoiceDataMode': ''}, None)

    # Extract UUID
    uuid = helper.track_uuid(elem)


    # Extract SIM details
    sim_details = helper.get_elements_after_key(elem, 'sim', 'dict')
    sim_data = ''
    if sim_details:
        sim_data = helper.extract_value_from_string_or_dict(elem, 'sim')

    # Construct the result
    result = {
        'Action': 'SetVoiceDataMode',
        'SIMDetails': sim_data,
    }

    # Append custom output name if available
    custom_output_name = helper.track_custom_name(elem)
    if custom_output_name:
        result['Output Name'] = custom_output_name

    return helper.append_data(result, uuid)

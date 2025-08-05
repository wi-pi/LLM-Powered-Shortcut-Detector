import parse_xml.parse_shortcut_WF as helper
import parse_xml_output.parse_output_to_natural_language as output_helper


def action_setvolume(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Set': 'Media', 'volume to': '50%'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # get what to set
    set_volume = helper.extract_value_from_string_or_dict(elem, 'WFVolumeSetting')
    if set_volume is None:
        set_volume = 'Media'

    # Get the volume
    volume = helper.extract_value_from_string_or_dict(elem, 'WFVolume')
    if volume is None:
        volume = '50%'
    else:
        if type(volume) == list:
            volume = output_helper.parse_get_attachment(volume)
        else:
            volume = f"{volume * 100}%"

    res = {'Set': set_volume, 'volume to': volume}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
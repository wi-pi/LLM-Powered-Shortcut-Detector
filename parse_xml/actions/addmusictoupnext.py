import parse_xml.parse_shortcut_WF as helper
import parse_xml_output.parse_output_to_natural_language as parse_output



def action_addmusictoupnext(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Add': '', 'to': 'Next of Playing Next'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the music
    music = helper.extract_value_from_string_or_dict(elem, 'WFMusic')
    if music is None:
        music = ''

    res = {'Add': music}

    # Get when to play
    when = helper.extract_value_from_string_or_dict(elem, 'WFWhenToPlay')
    if when is None:
        when = 'Next of Playing Next'
    else:
        if type(when) == list:
            when = parse_output.parse_get_attachment(when)
        when = f"{when} of Playing Next"
    res['to'] = when

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
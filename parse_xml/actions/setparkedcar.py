import parse_xml.parse_shortcut_WF as helper


def action_setparkedcar(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Set Parked Car at': 'Current Location', 'Note': '', 'Image': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output name if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the set parked car at\set_parked_car_at = 'Current Location'
    set_parked_car_at = 'Current Location'
    loca_elem = helper.get_elements_after_key(elem, 'WFLocation', 'dict')
    if loca_elem is not None:
        set_parked_car_at = helper.parse_location_wfinput(loca_elem[0])
    # if set_parked_car_at is None:
    #     set_parked_car_at = 'Current Location'

    # Get the note
    note = helper.extract_value_from_string_or_dict(elem, 'WFSetParkedCarNotes')
    if note is None:
        note = ''

    # Get the image
    image = helper.extract_value_from_string_or_dict(elem, 'WFImage')
    if image is None:
        image = ''

    res = {'Set Parked Car at': set_parked_car_at, 'Note': note, 'Image': image}
    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)

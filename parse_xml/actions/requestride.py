import parse_xml.parse_shortcut_WF as helper


def action_requestride(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'From': 'Current Location', 'To': '', 'with': '', '# of Person': 1}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output name if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the pickup location
    pickup_location = 'Current Location'
    pickup_location_dict = helper.get_elements_after_key(elem, 'PickupLocation', 'dict')
    if pickup_location_dict is not None:
        pickup_location = helper.parse_location_wfinput(pickup_location_dict[0])

    res = {'From': pickup_location}

    # Get the dropoff location
    dropoff_location = ''
    dropoff_location_dict = helper.get_elements_after_key(elem, 'DropOffLocation', 'dict')
    if dropoff_location_dict is not None:
        dropoff_location = helper.parse_location_wfinput(dropoff_location_dict[0])

    res['To'] = dropoff_location

    # Get the app
    app = ''
    app_elem = helper.get_elements_after_key(elem, 'IntentAppDefinition', 'dict')
    if app_elem is not None:
        app = helper.parse_app_input(app_elem[0])

    res['with'] = app

    # Get the number of person
    num_person = 1
    num_person_elem = helper.get_elements_after_key(elem, 'PartySize', 'real')
    if num_person_elem is not None:
        num_person = helper.extract_value(num_person_elem[0])

    res['# of Person'] = num_person

    # if the app is not '', get the ride type and payment method
    if app != '':
        ride_type = helper.extract_value_from_string_or_dict(elem, 'RideOption')
        if ride_type is None:
            ride_type = ''

        payment_method = helper.extract_value_from_string_or_dict(elem, 'PaymentMethod')
        if payment_method is None:
            payment_method = ''

        res['Ride Type'] = ride_type
        res['Payment Method'] = payment_method

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
import parse_xml.parse_shortcut_WF as helper


def action_generatebarcode(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Generate QR code from': '', 'Error Correction': ''}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Find if the element have custom output name
    custom_output_name = helper.track_custom_name(elem)

    # Get the barcode data
    barcode_data = helper.extract_value_from_string_or_dict(elem, 'WFText')
    if barcode_data is None:
        barcode_data = ''

    # Get the error correction level
    error_correction = helper.extract_value_from_string_or_dict(elem, 'WFQRErrorCorrectionLevel')
    if error_correction is None:
        error_correction = 'Medium'

    res = {'Generate QR code from': barcode_data, 'Error Correction': error_correction}

    if custom_output_name is not None:
        res['Output Name'] = custom_output_name
    return helper.append_data(res, uuid)
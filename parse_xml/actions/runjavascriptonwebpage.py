import parse_xml.parse_shortcut_WF as helper


def action_runjavascriptonwebpage(elem):
    if not helper.check_validation(elem):
        return helper.append_data({'Run JavaScript on': '', 'Script': 'var result = [];\n// Get all links from the page\nvar elements = document.querySelectorAll("a");\nfor (let element of elements) {\n    result.push({\n        "url": element.href,\n        "text": element.innerText\n    });\n}\n\n// Call completion to finish\ncompletion(result);'}, None)

    # Check UUID
    uuid = helper.track_uuid(elem)

    # Get the custom output name if have
    custom_output_name = helper.track_custom_name(elem)

    # Get the input
    input_text = helper.extract_value_from_string_or_dict(elem, 'WFInput')
    if input_text is None:
        input_text = ''

    # Get the JavaScript
    javascript = helper.extract_value_from_string_or_dict(elem, 'WFJavaScript')
    if javascript is None:
        javascript = 'var result = [];\n// Get all links from the page\nvar elements = document.querySelectorAll("a");\nfor (let element of elements) {\n    result.push({\n        "url": element.href,\n        "text": element.innerText\n    });\n}\n\n// Call completion to finish\ncompletion(result);'

    res = {'Run JavaScript on': input_text, 'Script': javascript}
    if custom_output_name is not None:
        res['Output Name'] = custom_output_name

    return helper.append_data(res, uuid)
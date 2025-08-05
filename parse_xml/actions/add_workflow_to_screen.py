import parse_xml.parse_shortcut_WF as helper
from parse_xml.init_parser import PlistParser
import xml.etree.ElementTree as ET

def parse_specific_dict_element(filename, element):
    # Read the XML content from the file
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            xml_content = file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {filename} was not found.")

    # Initialize the PlistParser with the XML content
    parser = PlistParser(xml_content)
    if parser.root.tag != 'plist':
        raise ValueError("The XML root element must be 'plist'. Please check the file content.")

    # Parse only the specified dict element directly
    if element.tag != 'dict':
        raise ValueError("The provided element is not a 'dict' element.")

    # Parse and return the specified dictionary element
    parsed_dict = parser.parse_dict(element)
    return parsed_dict

def action_add_workflow_to_screen(elem, file_name):
    return parse_specific_dict_element(file_name, elem)
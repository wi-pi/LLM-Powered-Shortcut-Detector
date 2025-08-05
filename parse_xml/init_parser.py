import sys
import xml.etree.ElementTree as ET
from datetime import datetime
import base64

class PlistParser:
    def __init__(self, xml_content):
        self.root = ET.fromstring(xml_content)
        if self.root.tag != 'plist':
            raise ValueError("Root element must be 'plist'")
        self.version = self.root.attrib.get('version', '1.0')
        self.data = self.parse_element(self.root.find('./'))

    def parse_element(self, element):
        if element is None:
            return None

        tag = element.tag
        if tag == 'array':
            return [self.parse_element(child) for child in element]
        elif tag == 'dict':
            return self.parse_dict(element)
        elif tag == 'key':
            return element.text
        elif tag == 'string':
            return element.text or ''
        elif tag == 'data':
            return base64.b64decode(''.join(element.text.strip().split()))
        elif tag == 'date':
            return self.parse_date(element.text)
        elif tag == 'true':
            return True
        elif tag == 'false':
            return False
        elif tag == 'real':
            return float(element.text)
        elif tag == 'integer':
            return int(element.text)
        else:
            raise ValueError(f"Unknown element: {tag}")

    def parse_dict(self, element):
        elements = list(element)
        d = {}
        i = 0
        while i < len(elements):
            key_elem = elements[i]
            if key_elem.tag != 'key':
                raise ValueError("Expected 'key' element in 'dict'")
            key = key_elem.text
            i += 1
            if i >= len(elements):
                raise ValueError("Value missing for key in 'dict'")
            value_elem = elements[i]
            value = self.parse_element(value_elem)
            d[key] = value
            i += 1
        return d

    def parse_date(self, date_str):
        formats = [
            '%Y-%m-%dT%H:%M:%SZ',
            '%Y-%m-%dT%H:%MZ',
            '%Y-%m-%dT%HZ',
            '%Y-%m-%dZ',
        ]
        for fmt in formats:
            try:
                return datetime.strptime(date_str, fmt)
            except ValueError:
                continue
        raise ValueError(f"Date '{date_str}' is not in a recognized ISO 8601 format")

# def parse_plist(content):
#     parser = PlistParser(content)
#     return parser.data

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

# Example usage:
if __name__ == "__main__":
    xml_content = sys.argv[1]
    parser = PlistParser(xml_content)
    print(parser.data)



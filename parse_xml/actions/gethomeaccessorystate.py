from parse_xml.init_parser import parse_specific_dict_element


def action_gethomeaccessory(elem, file_name):
    return parse_specific_dict_element(file_name, elem)
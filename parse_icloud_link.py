import sqlite3
import requests
import os
import time
import subprocess
import json
import plistlib


def modify_icloud_url(url):
    # Modify the iCloud URL to access the API
    if "https://www.icloud.com/shortcuts/" in url:
        return url.replace("https://www.icloud.com/shortcuts/", "https://www.icloud.com/shortcuts/api/records/")
    return None


def download_json_data(api_url):
    try:
        # Send a GET request to the API URL
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Failed to download JSON data from {api_url}: {e}")
        return None


def extract_shortcut_info(json_data):
    try:
        download_url = json_data['fields']['shortcut']['value']['downloadURL']
        name = json_data['fields']['name']['value']
        return download_url, name
    except KeyError as e:
        print(f"Failed to extract shortcut info: {e}")
        return None, None


def download_shortcut_file(url, file_path):
    try:
        # Send a GET request to download the file
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        with open(file_path, 'wb') as file:
            file.write(response.content)
        return True
    except requests.exceptions.RequestException as e:
        print(f"Failed to download shortcut file from {url}: {e}")
        return False


def convert_plist_to_xml(plist_path, xml_path):
    try:
        # Load the plist (binary or XML) from file
        with open(plist_path, 'rb') as f_in:
            plist_data = plistlib.load(f_in)

        # Write it back out in XML format
        with open(xml_path, 'wb') as f_out:
            plistlib.dump(plist_data, f_out, fmt=plistlib.FMT_XML)

        return True
    except Exception as e:
        print(f"Failed to convert plist to XML with plistlib: {e}")
        return False


def run(link, output_dir=None):
    link = modify_icloud_url(link)

    # Extract shortcut info and name
    shortcut_info, original_name = extract_shortcut_info(download_json_data(link))

    # Create a timestamp
    timestamp = int(time.time())  # Unix timestamp for uniqueness

    # Construct the filename using original name and timestamp
    filename = f"{original_name}_{timestamp}.plist"

    # If output_dir is specified, prepend it to the filename
    if output_dir:
        filename = os.path.join(output_dir, filename)

    # Download and convert the shortcut file
    download_shortcut_file(shortcut_info, filename)
    xml_filename = filename.replace('.plist', '.xml')
    convert_plist_to_xml(filename, xml_filename)

    # Clean up the intermediate plist file
    try:
        os.remove(filename)
    except OSError:
        pass

    return xml_filename


# Example usage
if __name__ == "__main__":
    run('https://www.icloud.com/shortcuts/0854ca93a7fd4d1bbd44a2f895e1b4b2')
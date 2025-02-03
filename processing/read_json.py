"""
This module provides functionality to read and parse JSON files.

Functions:
    open_json_file(file_path: str) -> dict:
        Opens a JSON file, parses its content, and returns it as a dictionary.
        If the file is not found or contains invalid JSON, an error message is
        printed and an empty dictionary is returned.
"""
import json


def open_json_file(file_path: str) -> dict:
    try:
        with open(file_path, "r") as file:
            json_data = json.load(file)

            # print("Config file opened successfully")
            # print(f"Config data: {json_data}")

    except (FileNotFoundError, json.JSONDecodeError):
        print("Error: File not found, unable to open or invalid json format")
        return {}

    file.close()

    return json_data

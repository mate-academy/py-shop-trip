import json
import os


def config_reader(current_dir: str, filename: str) -> dict:
    config_file_path = os.path.join(current_dir, filename)

    try:
        with open(config_file_path, "r") as config_file:
            config_dict = json.load(config_file)
        return config_dict
    except FileNotFoundError:
        print(f"File '{config_file_path}' not found.")

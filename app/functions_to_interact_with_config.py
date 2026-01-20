import json
import os


def get_file_config(config_we_need: str) -> dict:
    if os.path.exists("app/config.json"):
        with open("app/config.json") as json_data_file:
            all_config = json.load(json_data_file)

            config = {
                config: all_config[config]
                for config in all_config
                if config == config_we_need
            }
            return config
    else:
        raise FileNotFoundError("config.json not found")


def get_file_dict(data: dict, key: str) -> dict:
    items = data.get(key, [])
    new_data = data.copy()

    new_data.pop(key, None)

    for i, item in enumerate(items, start=1):
        item_key = item.get("name", f"{key[:-1]}{i}")
        new_data[item_key] = item

    return new_data

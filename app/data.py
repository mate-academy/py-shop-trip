import json


def get_data() -> dict:
    with open("app/config.json", "r") as data_file:
        data_dict = json.load(data_file)
    return data_dict


data = get_data()

import json


def get_information() -> dict:
    with open("app/config.json", "r") as file:
        info = json.load(file)
        return info


fuel_price = get_information()["FUEL_PRICE"]


def get_customers_list() -> list:
    return get_information()["customers"]


def get_shops_list() -> list:
    return get_information()["shops"]

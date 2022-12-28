import json


def get_information() -> dict:
    with open("app/config.json") as f:
        information = json.load(f)
        return information


def get_customers() -> list:
    cust_dict = get_information()
    return cust_dict["customers"]


def get_shops() -> list:
    cust_dict = get_information()
    return cust_dict["shops"]


def get_fuel_price() -> list:
    cust_dict = get_information()
    return cust_dict["FUEL_PRICE"]

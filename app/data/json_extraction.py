import json


def extract_data() -> dict:
    with open("app/data/config.json", "r") as data_in:
        return json.load(data_in)


data = extract_data()
FUEL_PRICE = data["FUEL_PRICE"]
customers = data["customers"]
shops = data["shops"]

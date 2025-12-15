import json


def loader(file_name: str) -> tuple:
    with open(file_name) as file:
        result = json.load(file)
    fuel_price = result.get("FUEL_PRICE")
    customers = result.get("customers")
    shops = result.get("shops")

    return fuel_price, customers, shops

import json
from app.shop import Shop
from app.customer import Customer
from pathlib import Path


def unpack_from_json():
    base_dir = Path(__file__).resolve().parent
    with open(base_dir / "config.json") as file:
        json_content = json.load(file)
    fuel_price = json_content["FUEL_PRICE"]
    customers = [Customer(*customer.values())
                 for customer in json_content["customers"]]
    shops = [Shop(*shop.values()) for shop in json_content["shops"]]
    return {"FUEL_PRICE": fuel_price, "customers": customers, "shops": shops}


def shop_trip():
    data = unpack_from_json()
    for customer in data["customers"]:
        print(f"{customer.name} has {customer.money} dollars")
        cheapest_shop = customer.find_cheapest_trip(
            data["shops"], data['FUEL_PRICE']
        )
        if cheapest_shop["costs"] > customer.money:
            print(f"{customer.name} doesn't have enough money"
                  f" to make purchase in any shop")
        else:
            customer.go_to_shop_trip(
                cheapest_shop["shop"], cheapest_shop["costs"])


shop_trip()

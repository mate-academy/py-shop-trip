import json

from pathlib import Path
from app.which_shop import Shop, Customer


def shop_trip():
    base_dir = Path(__file__).resolve().parent
    with open(base_dir / "config.json") as file:
        dct = json.load(file)
        for customer in dct["customers"]:
            shops = {}
            costs = []
            print(f"{customer['name']} has {customer['money']} dollars")
            for shop in dct["shops"]:
                trip_cost = Shop(shop, dct).trip_cost(customer)
                shop_info = {shop["name"]: trip_cost}
                shops.update(shop_info)
                costs.append(trip_cost)
                print(f"{customer['name']}'s trip to "
                      f"the {shop['name']} costs {trip_cost}")
            Customer(customer, costs, dct).which_shop(shops)


shop_trip()

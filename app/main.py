# import math
import json
# from datetime import datetime
from app.which_shop import Shop, WhichShop


def shop_trip():
    with open("app/config.json") as file:
        dct = json.load(file)
        for customer in dct["customers"]:
            shops = {}
            costs = []
            print(f"{customer['name']} has {customer['money']} dollars")
            for shop in dct["shops"]:
                trip_cost = Shop(customer, shop, dct).trip_cost()
                shop_info = {shop["name"]: trip_cost}
                shops.update(shop_info)
                costs.append(trip_cost)
                print(f"{customer['name']}'s trip to "
                      f"the {shop['name']} costs {trip_cost}")
            WhichShop(costs, customer, shops, shop, dct).which_shop()


shop_trip()

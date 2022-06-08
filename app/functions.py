import json

from app.classes import Customer, Shop


def read_info_from_json():

    list_of_customers = []
    list_of_shops = []

    with open("../app/config.json") as f:
        data = json.load(f)

    for customer in data["customers"]:
        list_of_customers.append(Customer(*customer.values()))

    for shop in data["shops"]:
        list_of_shops.append(Shop(*shop.values()))

    return {"list_of_customers": list_of_customers,
            "list_of_shops": list_of_shops,
            "fuel_cost": data['FUEL_PRICE']}

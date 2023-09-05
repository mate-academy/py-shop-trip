import json
from os import path
from app.customer import Customer
from app.shop import Shop


def loading_config_json() -> dict:
    parent_dir = path.dirname(__file__)
    with open(path.join(parent_dir, "config.json")) as file:
        config = json.load(file)
    return config


def shop_trip() -> None:
    config = loading_config_json()
    fuel_price = config["FUEL_PRICE"]
    customers = [
        Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            customer["car"]
        ) for customer in config["customers"]
    ]
    shops = [
        Shop(
            shop["name"],
            shop["location"],
            shop["products"]
        ) for shop in config["shops"]
    ]
    travel_shop = None
    for customer in customers:
        customer.print_amount_of_money()
        min_cost_trip = None
        for shop in shops:
            cost_trip = customer.cost_trip_for_the_products(shop, fuel_price)
            if min_cost_trip is None or cost_trip < min_cost_trip:
                min_cost_trip = cost_trip
                travel_shop = shop
        if min_cost_trip > customer.money:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")
            continue
        print(f"{customer.name} rides to {travel_shop.name}\n")
        travel_shop.receipt_printing(customer.name, customer.product_cart)
        print(f"{customer.name} rides home\n"
              f"{customer.name} now has "
              f"{customer.money - min_cost_trip} dollars\n")

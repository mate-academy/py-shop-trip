import json

import os

from app.shop import Shop

from app.customer import Customer

from app.car import Car


config_path = os.path.join(os.path.dirname(__file__), "config.json")


def shop_trip() -> None:

    with open(config_path, "r") as json_file:
        task_info = json.load(json_file)

    fuel_price = task_info.get("FUEL_PRICE")
    customers = task_info.get("customers")
    shops = task_info.get("shops")

    shops = [Shop(shop["name"],
                  shop["location"],
                  shop["products"]) for shop in shops]
    customers = [Customer(customer["name"],
                          customer["product_cart"],
                          customer["location"],
                          customer["money"],
                          Car(**customer["car"])) for customer in customers]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        all_shop = {}
        for shop in shops:
            shop_price = shop.shop_total_coast(customer.product_cart)
            distance = customer.find_distance(shop.location)
            total_cost = (
                round(customer.car.coast_trip(distance,
                                              fuel_price) * 2 + shop_price, 2))
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {total_cost}")
            all_shop[shop] = total_cost
        cheapest_shop = min(all_shop, key=all_shop.get)
        if all_shop[cheapest_shop] > customer.money:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")
        else:
            print(f"{customer.name} rides to {cheapest_shop.name}\n")
            current_location = cheapest_shop.location
            cheapest_shop.print_check(customer.name, customer.product_cart)
            customer.rides_home(all_shop[cheapest_shop], current_location)


shop_trip()

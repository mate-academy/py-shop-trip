import json
import os

from math import dist

from app.customer import Customer
from app.shop import Shop
from app.car import Car


def shop_trip() -> None:
    for dirpath, dirnames, filenemas in os.walk("/"):
        if "config.json" in filenemas:
            path_to_file = os.path.abspath(
                os.path.join(dirpath, "config.json")
            )
            with open(path_to_file, "r") as f:
                data = json.load(f)
                break

    fuel_price = data("FUEL_PRICE")
    _customers = data("customers")
    _shops = data("shops")

    shops: list[Shop] = []
    for _shop in _shops:
        shop = Shop(
            name=_shop["name"],
            location=_shop["location"],
            products=_shop["products"]
        )
        shops.append(shop)

    for _customer in _customers:
        customer = Customer(
            name=_customer["name"],
            product_cart=_customer["product_cart"],
            location=_customer["location"],
            money=_customer["money"],
            car=Car(
                brand=_customer["car"]["brand"],
                fuel_consumption=_customer["car"]["fuel_consumption"]
            )
        )
        print(f"{customer.name} has {customer.money} dollars")
        costs = []
        for shop in shops:
            distance_km = dist(customer.location, shop.location)
            fuel_cost = (
                customer.car.calculate_fuel_cost(distance_km, fuel_price)
            )
            trip_cost = (
                2 * fuel_cost
                + shop.calculate_cart_price(customer.product_cart)
            )

            rounded_trip_cost = round(trip_cost, 2)
            print(
                f"{customer.name}'s trip to the {shop.name} "
                f"costs {rounded_trip_cost}"
            )
            costs.append(rounded_trip_cost)

        if customer.money >= min(costs):
            min_index = costs.index(min(costs))
            target_shop: Shop = shops[min_index]
            print(f"{customer.name} rides to {target_shop.name}\n")
            customer.change_location(target_shop.location)
            target_shop.print_receipt(customer)
            print(f"{customer.name} rides home")
            customer.change_location(customer.home)
            remaining_money = customer.money - min(costs)
            print(f"{customer.name} now has {remaining_money} dollars\n")
        else:
            print(
                f"{customer.name} doesn't have enough money "
                "to make a purchase in any shop"
            )

import json
import os

from app.car import Car
from app.shop import Shop
from app.customer_class import Customer


current_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(current_dir, "config.json")


def shop_trip() -> None:
    with open(config_path, "r") as f:
        data = json.load(f)

    fuel_price = data["FUEL_PRICE"]

    customers = []

    for people in data["customers"]:
        car = Car(
            brand=people["car"]["brand"],
            fuel_consumption=people["car"]["fuel_consumption"]
        )
        customer = Customer(
            name=people["name"],
            product_cart=people["product_cart"],
            location=people["location"],
            money=people["money"],
            car=car
        )
        customers.append(customer)

    shop_list = [
        Shop(
            shop["name"],
            shop["location"],
            shop["products"]
        ) for shop in data["shops"]
    ]

    for customer in customers:
        print(f"{customer.name} has {round(customer.money, 2)} dollars")

        for shop in shop_list:
            trip_cost, products_cost, fuel_cost =\
                customer.calculate_total_trip_cost(shop, fuel_price)
            print(f"{customer.name}'s trip to "
                  f"the {shop.name} costs{trip_cost: .2f}")

        min_trip_cost = float("inf")
        chosen_shop = None
        for shop in shop_list:
            trip_cost, products_cost, fuel_cost =\
                customer.calculate_total_trip_cost(shop, fuel_price)
            if trip_cost < min_trip_cost:
                min_trip_cost = trip_cost
                chosen_shop = shop
        if min_trip_cost > customer.money:
            print(f"{customer.name} doesn't have enough"
                  f" money to make a purchase in any shop")
        else:
            print(f"{customer.name} rides to {chosen_shop.name}")
            print()
            customer.make_purchase(chosen_shop, fuel_price)

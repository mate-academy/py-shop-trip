import json

from app.car import Car
from app.customer import Customer
from app.shop import Shop
import os


def shop_trip() -> None:
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_path) as file:
        data = json.load(file)

    fuel_price = data["FUEL_PRICE"]

    shops = [
        Shop(
            shop["name"],
            shop["location"],
            shop["products"],
        )
        for shop in data["shops"]
    ]

    customers = []

    for customer in data["customers"]:
        car = Car(
            customer["car"]["brand"],
            customer["car"]["fuel_consumption"]
        )

        customers.append(
            Customer(
                customer["name"],
                customer["product_cart"],
                customer["location"],
                customer["money"],
                car,
            )
        )

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        cheapest_shop = None
        cheapest_cost = None

        for shop in shops:
            cost = customer.trip_cost(shop, fuel_price)

            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {cost:.2f}")

            if cheapest_cost is None or cost < cheapest_cost:
                cheapest_cost = cost
                cheapest_shop = shop

        if cheapest_cost > customer.money:
            print(
                f"{customer.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )
            continue

        customer.ride_to(cheapest_shop)

        customer.money -= cheapest_cost

        cheapest_shop.print_receipt(
            customer.name,
            customer.product_cart,
        )

        customer.ride_home()

        print(f"{customer.name} now has " f"{customer.money:.2f} dollars")

        print()

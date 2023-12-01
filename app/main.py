import json
import os

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(path, "r") as file_config:
        config = json.load(file_config)

    fuel_price = config["FUEL_PRICE"]

    for client in config["customers"]:
        customer = Customer(
            name=client["name"],
            product_cart=client["product_cart"],
            location=client["location"],
            money=client["money"]
        )

        car = Car(
            fuel_consumption=client["car"]["fuel_consumption"],
        )

        print(f"{customer.name} has {customer.money} dollars")
        min_cost, data_shop = customer.money, ""

        for item in config["shops"]:
            shop = Shop(
                name=item["name"],
                location=item["location"],
                cost_products=item["products"]
            )
            cost_products = shop.get_cost_products(customer.product_cart)
            cost_trip = car.get_cost_trip(
                customer.location,
                shop.location,
                fuel_price
            )
            cost_trip_in_shop = cost_products + cost_trip
            print(f"{customer.name}'s trip to the {shop.name}"
                  f" costs {cost_trip_in_shop}")
            if cost_trip_in_shop < min_cost:
                min_cost, data_shop, = cost_trip_in_shop, shop
                shop_name = shop.name

        if min_cost < customer.money:
            print(f"{customer.name} rides to {shop_name}")
            customer.buy_in_shop(min_cost, data_shop)
        else:
            print(
                f"{customer.name} "
                f"doesn't have enough money to make a "
                f"purchase in any shop"
            )


if __name__ == "__main__":
    shop_trip()

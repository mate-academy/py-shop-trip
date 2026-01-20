import json

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open(
            "app/config.json",
            "r"
    ) as file:
        config = json.load(file)

    fuel_price = config["FUEL_PRICE"]

    customers = []
    for customer in config["customers"]:
        car = Car(
            customer["car"]["brand"],
            customer["car"]["fuel_consumption"]
        )
        customer = Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            car
        )
        customers.append(customer)

    shops = []
    for shop in config["shops"]:
        shop = Shop(shop["name"], shop["location"], shop["products"])
        shops.append(shop)

    for customer in customers:
        shop = customer.cheapest_shopping(shops, fuel_price)
        if not (
                customer.money
                >= customer.calculate_trip_cost(shop, fuel_price)
        ):
            print(
                f"{customer.name} "
                f"doesn't have enough money to make a purchase in any shop"
            )
            return
        print(f"{customer.name} rides to {shop.name}\n")
        customer.shopping(shop, fuel_price)

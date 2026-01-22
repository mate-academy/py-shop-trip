import json
import os

from app.customer import Customer
from app.shop import Shop
from app.car import Car


def shop_trip() -> None:
    base_dir = os.path.dirname(os.path.abspath(__file__))

    config_path = os.path.join(base_dir, "config.json")
    with open(config_path, "r") as file:
        config = json.load(file)

    fuel_price = config.get("FUEL_PRICE")
    shops = []

    for shop in config.get("shops"):
        name = shop.get("name")
        products = shop.get("products")
        location = shop.get("location")

        shops.append(Shop(name, location, products))

    for client in config.get("customers"):
        name = client.get("name")
        product_cart = client.get("product_cart")
        location = client.get("location")
        money = client.get("money")
        car = Car(fuel_price=fuel_price, **client.get("car"))

        customer = Customer(name, product_cart, location, money, car)

        print(f"{name} has {money} dollars")

        trip_result = customer.find_cheapest_trip(shops)

        shop_name = trip_result[0]
        cheapest_shop = trip_result[1]
        money_spend = trip_result[2]

        if customer.money < money_spend:
            print(
                f"{customer.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )
            continue

        print(f"{name} rides to {shop_name}")

        customer.location = cheapest_shop.location

        print("")

        cheapest_shop.print_bill(customer)

        print("")

        print(f"{name} rides home")

        customer.location = customer.home_location
        customer.money = round(customer.money - money_spend, 2)

        print(f"{name} now has {customer.money} dollars")

        print("")

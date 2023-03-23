import json

from app.customer import Customer
from app.car import Car
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as config_file:

        config_dict = json.load(config_file)

        shops = [
            Shop(shop["name"], shop["location"], shop["products"])
            for shop in config_dict["shops"]
        ]

        for customer in config_dict["customers"]:
            customer_obj = Customer(customer["name"],
                                    customer["product_cart"],
                                    customer["location"],
                                    customer["money"],
                                    Car(customer["car"]["brand"],
                                        customer["car"]["fuel_consumption"]),
                                    config_dict["FUEL_PRICE"])

            cheapest_shop = customer_obj.pick_shop(shops)
            if cheapest_shop is None:
                continue

            customer_obj.location = cheapest_shop.location
            cheapest_shop.buy_products(customer_obj.name,
                                       customer_obj.product_cart)

            customer_obj.location = customer["location"]
            customer_obj.go_home(cheapest_shop)

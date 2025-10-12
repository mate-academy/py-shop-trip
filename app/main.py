import json

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as config_file:
        config = json.load(config_file)
        fuel_price = config["FUEL_PRICE"]

        shops = [
            Shop(**shop)
            for shop in config["shops"]
        ]

        for customer in config["customers"]:
            customer_instance = (Customer(**customer))
            customer_instance.car = Car(**customer["car"])

            print(
                f"{customer_instance.name} "
                f"has {customer_instance.money} dollars"
            )
            cost, shop = customer_instance.calculate_cheapest_option(
                shops, fuel_price
            )

            if customer_instance.money >= cost:
                customer_instance.visit_shop(shop)
                customer_instance.make_a_purchase(shop, cost)
                customer_instance.go_home()
            else:
                print(
                    f"{customer_instance.name} "
                    f"doesn't have enough money "
                    f"to make a purchase in any shop"
                )

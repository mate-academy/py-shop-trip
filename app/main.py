import json
import os
from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open(
        os.path.join(os.path.dirname(__file__), "config.json"), "r"
    ) as config_file:
        config = json.load(config_file)
    goal_store = Shop(0, 0, 0)
    shops_list = [
        Shop(
            name=shop["name"],
            location=shop["location"],
            products=shop["products"],
        )
        for shop in config["shops"]
    ]

    for customer in config["customers"]:
        person = Customer(
            name=customer["name"],
            product_cart=customer["product_cart"],
            location=customer["location"],
            money=customer["money"],
            car=Car(
                brand=customer["car"]["brand"],
                fuel_consumption=customer["car"]["fuel_consumption"],
            ),
        )
        person.money_check()

        for shop in shops_list:
            shop.trip_price_counting(person, config["FUEL_PRICE"])
            if shop.full_price < goal_store.full_price:
                goal_store = shop

        if goal_store.full_price > person.money:
            print(
                f"{person.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )
        else:
            person.money -= goal_store.full_price
            goal_store.to_shop(person)
            goal_store.check(person)
            person.is_home()

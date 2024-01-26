import json

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as f:
        config = json.load(f)
    fuel_price = config["FUEL_PRICE"]

    customers = [
        Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            Car(customer["car"]["brand"], customer["car"]["fuel_consumption"])
        )
        for customer in config["customers"]
    ]

    shops = [
        Shop(
            shop["name"],
            shop["location"],
            shop["products"]
        )
        for shop in config["shops"]
    ]

    for customer in customers:
        optimal_shop = customer.find_optimal_shop(shops, fuel_price)
        if customer.money >= optimal_shop["total_cost"]:
            customer.has_enough_money(optimal_shop)
            continue
        customer.has_not_enough_money()

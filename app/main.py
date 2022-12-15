import json
from app.customer import Customer
from app.car import Car
from app.shop import Shop


def read_customers(data: dict) -> list[Customer]:
    return [
        Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            Car(
                customer["car"]["brand"],
                customer["car"]["fuel_consumption"],
            ),
        )
        for customer in data["customers"]
    ]


def read_shops(data: dict) -> list[Shop]:
    return [
        Shop(shop["name"], shop["location"], shop["products"])
        for shop in data["shops"]
    ]


def shop_trip() -> None:
    with open("app/config.json") as cfg:
        data = json.load(cfg)

    customers = read_customers(data)
    shops = read_shops(data)
    fuel_price = data["FUEL_PRICE"]

    for customer in customers:
        customer.print_money()
        for shop in shops:
            customer.print_costs_trip(shop, fuel_price)

        cheaper_shop = customer.get_cheaper_shop(shops, fuel_price)
        if customer.money < customer.calc_trip_price(cheaper_shop, fuel_price):
            print(
                f"{customer.name} doesn't have enough money"
                f" to make purchase in any shop"
            )
        else:
            customer.ride_to_shop(
                customer.get_cheaper_shop(shops, fuel_price), fuel_price
            )

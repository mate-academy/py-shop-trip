import json

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as input_file:
        base = json.load(input_file)

    fuel_price = base["FUEL_PRICE"]

    customers_base = [
        Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            Car(
                customer["car"]["brand"],
                customer["car"]["fuel_consumption"]
            )
        )
        for customer in base["customers"]
    ]

    shops_base = [
        Shop(
            shop["name"],
            shop["location"],
            shop["products"]
        )
        for shop in base["shops"]
    ]

    for customer in customers_base:
        customer.print_financial_status()
        customer.pick_the_cheapest(shops_base, fuel_price)


if __name__ == "__main__":
    shop_trip()

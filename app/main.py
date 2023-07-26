import json

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as input_file:
        base = json.load(input_file)

    fuel_price = base["FUEL_PRICE"]

    customers_base = []
    for customer in base["customers"]:
        customers_base.append(
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
        )

    shops_base = []
    for shop in base["shops"]:
        shops_base.append(
            Shop(
                shop["name"],
                shop["location"],
                shop["products"]
            )
        )

    for customer in customers_base:
        customer.print_financial_status()
        customer.pick_the_cheapest(shops_base, fuel_price)


if __name__ == "__main__":
    shop_trip()

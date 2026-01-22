import json

from app.car import Car
from app.shop import Shop
from app.customer import Customer


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        try:
            config = json.load(file)
        except FileNotFoundError:
            raise "File not found!"

    fuel_price = config.get("FUEL_PRICE")

    customers_data = config.get("customers")
    customers = [
        Customer(
            name=customer.get("name"),
            product_cart=customer.get("product_cart"),
            location=customer.get("location"),
            money=customer.get("money"),
            car=Car(**customer.get("car"))
        ) for customer in customers_data
    ]

    shops_data = config.get("shops")
    shops = [Shop(**shop) for shop in shops_data]

    for customer in customers:
        customer.find_cheapest_shop(shops, fuel_price)


if __name__ == "__main__":
    shop_trip()

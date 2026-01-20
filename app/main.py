import json

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        json_data = json.load(file)

    fuel_price = json_data["FUEL_PRICE"]

    customers = [
        Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            Car(
                customer["car"]["brand"],
                customer["car"]["fuel_consumption"]
            )
        ) for customer in json_data["customers"]]

    shops = [
        Shop(
            shop["name"],
            shop["location"],
            shop["products"]
        ) for shop in json_data["shops"]]

    for customer in customers:
        customer.has_money()
        customer.chip_shop(shops, fuel_price)


if __name__ == "__main__":
    shop_trip()

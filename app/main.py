import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("config.json", "r") as file:
        config = json.load(file)

    fuel_price = config["FUEL_PRICE"]
    customers = config["customers"]
    shops = config["shops"]

    shops_list = [Shop(
        shop["name"],
        shop["location"],
        shop["products"]
    ) for shop in shops]

    customers_list = [Customer(
        customer["name"],
        customer["product_cart"],
        customer["location"],
        customer["money"],
        customer["car"],
    ) for customer in customers]

    for customer in customers_list:
        customer.print_the_trip(fuel_price, shops_list)


shop_trip()

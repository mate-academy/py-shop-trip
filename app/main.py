import json
from app.shop import Shop
from app.customer import Customer
from app.shoppingCalculator import ShoppingCalculator


def shop_trip() -> None:

    with open("app/config.json") as file:

        json_data = json.load(file)

        for customer in json_data["customers"]:
            Customer(customer)

        for shop in json_data["shops"]:
            Shop(shop)

        fuel = json_data["FUEL_PRICE"]

    for customer in Customer.customers:
        cost = ShoppingCalculator(
            customer,
            Shop.shops,
            fuel
        )
        cost.get_shopping_price()

import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file_incoming:
        config_info = json.load(file_incoming)

    fuel_price = config_info["FUEL_PRICE"]

    customers: list[Customer] = [Customer(**customer) for customer in config_info["customers"]]
    shops: list[Shop] = [Shop(**shop) for shop in config_info["shops"]]

    for customer in customers:
        customer.car.fuel_price = fuel_price
        # find the cheapest shop
        customer.calculates_ultimate_shopping_journey_cost(shops)
        # print result based on customer's money
        customer.render_shop_journey()


if __name__ == "__main__":
    shop_trip()

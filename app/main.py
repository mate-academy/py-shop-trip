import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file_in:
        config_data = json.load(file_in)

    for customer in config_data["customers"]:
        Customer(**customer)

    for shop in config_data["shops"]:
        Shop(**shop)

    for customer in Customer.customers:
        for shop in Shop.shops:
            customer.car.fuel_price = config_data["FUEL_PRICE"]
            customer.calculates_full_shopping_trip_cost(shop)
        customer.display_shop_trip()


if __name__ == "__main__":
    shop_trip()

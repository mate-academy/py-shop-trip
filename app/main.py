import json
from app.customer import Customer
from app.shop import Shop
from app.car import Car


def shop_trip() -> None:
    full_path = (
        "C:\\Programming Study\\Mate\\py-shop-trip\\app\\" + "config.json"
    )
    with open(full_path, "r") as file_in:
        config_data = json.load(file_in)

    Car.FUEL_PRICE = config_data["FUEL_PRICE"]

    for customer in config_data["customers"]:
        Customer(**customer)
    for shop in config_data["shops"]:
        Shop(**shop)

    for customer in Customer.customers:
        for shop in Shop.shops:
            customer.calculates_full_shopping_trip_cost(shop)
        customer.display_shop_trip()


if __name__ == "__main__":
    shop_trip()

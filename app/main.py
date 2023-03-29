import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as read_file:
        data = json.load(read_file)
        fuel_price = data["FUEL_PRICE"]
        list_of_shop = [Shop(shop["name"],
                             shop["location"],
                             shop["products"])
                        for shop in data["shops"]]

        for customer in data["customers"]:
            new_customer = Customer(customer["name"],
                                    customer["product_cart"],
                                    customer["location"],
                                    customer["money"],
                                    customer["car"])

            new_customer.current_balance()
            new_customer.final_result(fuel_price, list_of_shop)


shop_trip()

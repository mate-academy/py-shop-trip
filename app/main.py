import json
import os

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    app_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(app_dir, "config.json")
    with open(path, "r") as config_file:
        config_dict = json.load(config_file)

    fuel_price = config_dict["FUEL_PRICE"]
    customers = []
    for customer in config_dict["customers"]:
        customer = Customer(
            name=customer["name"],
            products=customer["product_cart"],
            location=customer["location"],
            money=customer["money"],
            car=Car(
                customer["car"]["brand"],
                customer["car"]["fuel_consumption"],
            ),
        )
        customers.append(customer)
    shops = []
    for shop in config_dict["shops"]:
        shop = Shop(
            name=shop["name"],
            location=shop["location"],
            products=shop["products"],
        )
        shops.append(shop)

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        cheapest_shop = customer.choose_shop(shops, fuel_price)
        if not cheapest_shop:
            continue
        customer.buy_products(cheapest_shop, fuel_price)
        customer.return_home()


if __name__ == "__main__":
    shop_trip()

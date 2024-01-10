import json
from app.customer import Customer
from app.shop import Shop
from app.car import Car


def shop_trip() -> None:
    with open("app/config.json", "r") as config_file:
        data = json.load(config_file)

    fuel_price = data["FUEL_PRICE"]

    shops = [Shop(shop_data["name"],
                  shop_data["location"],
                  shop_data["products"])
             for shop_data in data["shops"]]

    customers = [
        Customer(
            customer_data["name"],
            customer_data["product_cart"],
            customer_data["location"],
            customer_data["money"],
            Car(customer_data["car"]["brand"],
                customer_data["car"]["fuel_consumption"])
        )
        for customer_data in data["customers"]
    ]

    for customer in customers:
        customer.make_purchase(shops, fuel_price)

import json
from app.customer import Customer
from app.car import Car
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json") as file:
        config = json.load(file)

    fuel_price = config["FUEL_PRICE"]
    shops = [Shop(**shop_info) for shop_info in config["shops"]]
    customers = [
        Customer(
            name=cust_info["name"],
            location=cust_info["location"],
            money=cust_info["money"],
            product_cart=cust_info["product_cart"],
            car=Car(**cust_info["car"]),
        )
        for cust_info in config["customers"]
    ]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        customer.try_to_shop(shops, fuel_price)


shop_trip()

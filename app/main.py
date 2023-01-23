import json

from app.customer import Customer
from app.shop import Shop
from app.car import Car


def shop_trip() -> None:

    with open("app/config.json", "r") as f:
        data = json.load(f)

    list_of_customers = []
    list_of_shops = []
    fuel_price = data["FUEL_PRICE"]

    for customer in data["customers"]:
        list_of_customers.append(Customer(
            name=customer["name"],
            product_cart=customer["product_cart"],
            location=customer["location"],
            money=customer["money"],
            car=Car(
                customer["car"]["brand"],
                customer["car"]["fuel_consumption"]
            )
        )
        )

    for shop in data["shops"]:
        list_of_shops.append(Shop(
            name=shop["name"],
            location=shop["location"],
            products=shop["products"]
        )
        )

    for customer in list_of_customers:
        customer.find_the_best_shop(list_of_shops, fuel_price)
        best_shop_name = list(customer.best_shop.keys())[0]
        if customer.money >= customer.best_shop[best_shop_name]:
            customer.has_enough_money()
            print()
        else:
            customer.has_not_enough_money()

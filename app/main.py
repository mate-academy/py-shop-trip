import json
from typing import Any
from app.customers_shops.shops import Shop
from app.customers_shops.customers import Customer


def create_customers_shops() -> Any:
    read_info = json.load(open("app/config.json"))
    customers = []
    shops = []
    for customer in read_info["customers"]:
        customers.append(Customer(
            FUEL_PRICE=read_info["FUEL_PRICE"],
            name=customer["name"],
            product_cart=customer["product_cart"],
            location=customer["location"],
            money=customer["money"],
            car=customer["car"]
        ))
    for shop in read_info["shops"]:
        shops.append(Shop(
            name=shop["name"],
            location=shop["location"],
            products=shop["products"]
        ))
    return customers, shops


def shop_trip() -> None:
    customers, shops = create_customers_shops()

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        for shop in shops:
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {customer.calc_price(shop)}")

        customer.purchase()

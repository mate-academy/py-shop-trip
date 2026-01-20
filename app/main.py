from app.customer import Customer
from app.shop import Shop
from app.car import Car

import json
import datetime


def get_from_json(location: str) -> tuple[list[Customer], list[Shop], float]:
    with open(location, "r") as file:
        data = json.load(file)

    customers = [
        Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            Car(customer["car"]["brand"], customer["car"]["fuel_consumption"]),
        )
        for customer in data["customers"]
    ]
    shops = [Shop(**shop) for shop in data["shops"]]
    fuel_price = data["FUEL_PRICE"]
    return customers, shops, fuel_price


def shop_trip() -> None:
    customers, shops, fuel_price = get_from_json("app/config.json")

    for customer in customers:

        best_price = float("inf")
        best_shop = None

        print(f"{customer.name} has {customer.money} dollars")

        for shop in shops:
            way_price = customer.calculate_way_price(shop.location, fuel_price)
            shop_price = shop.get_price(customer)
            total_price = way_price + shop_price
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {total_price}")
            if total_price < best_price:
                best_price = total_price
                best_shop = shop

        if customer.money >= best_price:
            print(f"{customer.name} rides to {best_shop.name}\n\n"
                  f"Date: {datetime.datetime.now():%d/%m/%Y %H:%M:%S}\n"
                  f"Thanks, {customer.name}, for your purchase!\n"
                  "You have bought:")
            for product, value in customer.product_cart.items():
                cost_product = (
                    best_shop.products[product]
                    * customer.product_cart[product]
                )
                if int(cost_product) == cost_product:
                    print(f"{value} {product}s for "
                          f"{int(cost_product)} dollars")
                else:
                    print(f"{value} {product}s for "
                          f"{cost_product} dollars")

            print(f"Total cost is {best_shop.get_price(customer)} dollars\n"
                  f"See you again!\n\n"
                  f"{customer.name} rides home\n"
                  f"{customer.name} now has "
                  f"{customer.money - best_price} dollars\n")

        else:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")

import json
import os

from datetime import datetime

from app.customer import Customer
from app.shop import Shop
from app.car import Car


def shop_trip() -> None:
    path = os.path.join("app", "config.json")
    with open(path, "r") as source:
        source_data = json.load(source)
    fuel_price = source_data["FUEL_PRICE"]
    customers = [
        Customer(
            name=customer["name"],
            product_cart=customer["product_cart"],
            location=customer["location"],
            money=customer["money"],
            car=Car(
                brand=customer["car"]["brand"],
                fuel_consumption=customer["car"]["fuel_consumption"]
            )
        )
        for customer in source_data["customers"]
    ]
    shops = [
        Shop(
            name=shop["name"],
            location=shop["location"],
            products_price=shop["products"]
        )
        for shop in source_data["shops"]
    ]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        lowest_price = []
        for shop in shops:
            bill_on_each_product = shop.make_a_bill(customer.product_cart)
            current_trip_price = round(
                (sum(bill_on_each_product.values())
                 + customer.count_money_for_fuel(
                    shop_location=shop.location,
                    fuel_price=fuel_price) * 2),
                2)
            lowest_price.append((current_trip_price,
                                 shop.name,
                                 bill_on_each_product))
            print(f"{customer.name}'s trip to the {shop.name}"
                  f" costs {current_trip_price}")
        trip_price, name_shop, price_each_product = min(lowest_price)
        if customer.money < trip_price:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")
            continue
        customer.money -= trip_price
        print(f"{customer.name} rides to {name_shop}\n\n"
              f"Date: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
              f"Thanks, {customer.name}, for your purchase!\n"
              f"You have bought:"
              )
        for product in customer.product_cart:
            print(f"{customer.product_cart[product]} {product}s"
                  f" for {price_each_product[product]} dollars")
        print(f"Total cost is {sum(price_each_product.values())} dollars\n"
              f"See you again!\n\n"
              f"{customer.name} rides home\n"
              f"{customer.name} now has {customer.money} dollars\n")

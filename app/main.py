from __future__ import annotations
import json

from app.customer import Customer
from app.shop import Shop


FILE_NAME = "app/config.json"


def shop_trip() -> None:
    data = None
    with open(FILE_NAME, "r") as reader:
        data = json.load(reader)
    fuel_price = data.get("FUEL_PRICE")
    customers = [
        Customer(**customer)
        for customer in data.get("customers")
    ]
    shops = [Shop(**shop) for shop in data.get("shops")]
    for i, customer in enumerate(customers):
        if i > 0:
            print()
        print(f"{customer.name} has {customer.money} dollars")

        total_price, selected_shop = customer.money + 0.01, None
        for shop in shops:
            trip_price = customer.car.estimate_trip_price(
                fuel_price,
                customer.location,
                shop.location
            )
            cart_price = shop.calculate_cart_price(customer.products)
            print((
                f"{customer.name}'s trip to the {shop.name} "
                f"costs {trip_price + cart_price}"
            ))
            if trip_price + cart_price < total_price:
                total_price = trip_price + cart_price
                selected_shop = shop
        if selected_shop is None:
            print(
                f"{customer.name} doesn't have enough money "
                "to make purchase in any shop"
            )
            continue

        print(f"{customer.name} rides to {selected_shop.name}")
        customer.ride(selected_shop.location)
        selected_shop.checkout(customer.name, customer.products)
        print(f"{customer.name} rides home")
        customer.ride("back")
        customer.pay(total_price)
        print(f"{customer.name} now has {customer.money} dollars")

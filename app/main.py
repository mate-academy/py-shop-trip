# flake8: noqa
import json
import datetime # like in the checklist
from app.car import Car
from app.shop import Shop
from decimal import Decimal
from app.customer import Customer


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        data = json.load(file)

    Car.fuel_price = Decimal(str(data.get("FUEL_PRICE")))
    customers_list = [
        Customer(
            customer.get("name"),
            customer.get("product_cart"),
            customer.get("location"),
            customer.get("money"),
            customer.get("car")
        )
        for customer in data.get("customers")
    ]

    shops_list = [
        Shop(
            shop.get("name"),
            shop.get("location"),
            shop.get("products")
        )
        for shop in data.get("shops")
    ]

    for customer in customers_list:
        print(f"{customer.name} has {customer.money} dollars")
        trips_prices = {}

        for shop in shops_list:
            price = customer.go_to_trip(shop)
            if price is None:
                continue
            print(f"{customer.name}'s trip to the {shop.name} costs {round(float(price), 2)}")
            trips_prices[shop] = round(float(price), 2)

        best_trip = min(trips_prices, key=trips_prices.get)
        if not trips_prices[best_trip] <= customer.money:
            print(f"{customer.name} doesn't have enough money to make a purchase in any shop")
            return
        customer.money -= Decimal(str(trips_prices[best_trip]))
        print(f"{customer.name} rides to {best_trip.name}\n")

        print(f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        best_trip.buy_products(
            customer,
            message=True,
        )
        print()
        print(f"{customer.name} rides home")
        print(f"{customer.name} now has {customer.money} dollars")
        print()

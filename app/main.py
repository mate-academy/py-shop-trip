import json

from pathlib import Path

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    config_path = Path(__file__).with_name("config.json")

    with open(config_path, "r") as file:
        data = json.load(file)
        shops: list[Shop] = []
        for shop in data["shops"]:
            shops.append(Shop(
                name=shop["name"],
                location=shop["location"],
                products=shop["products"],
            ))

        customers: list[Customer] = []
        for customer in data["customers"]:
            car_data = customer["car"]
            car = Car(
                brand=car_data["brand"],
                fuel_consumption=car_data["fuel_consumption"],
            )

            customers.append(Customer(
                name=customer["name"],
                product_cart=customer["product_cart"],
                location=customer["location"],
                money=customer["money"],
                car=car,
            ))

    for customer in customers:
        money = customer.money
        print(f"{customer.name} has {customer.money} dollars")

        lowest_cost = float("inf")
        cheapest_shop: Shop | None = None
        for shop in shops:
            trip_price = customer.calculate_trip_cost(
                shop,
                data["FUEL_PRICE"],
            )

            print(
                f"{customer.name}'s trip to the {shop.name} costs "
                f"{trip_price:.2f}"
            )

            if lowest_cost > trip_price:
                lowest_cost = trip_price
                cheapest_shop = shop
        if cheapest_shop is None:
            continue
        if money < lowest_cost:
            print(
                f"{customer.name} doesn't have enough money "
                "to make a purchase in any shop"
            )
            continue

        customer.ride(cheapest_shop.location)

        print(f"{customer.name} rides to {cheapest_shop.name}")
        print()

        cheapest_shop.print_receipt(
            customer_name=customer.name,
            product_cart=customer.product_cart,
        )
        print()

        customer.to_house()
        print(f"{customer.name} rides home")

        customer.pay(lowest_cost)
        print(
            f"{customer.name} now has "
            f"{round(customer.money, 2)} dollars"
        )
        print()

# main.py
from app.shop import Shop
from app.customer import Customer
from app.car import Car

import json
from typing import Dict


def extract_config_data() -> Dict:
    with open("config.json", "r") as f:
        data = json.load(f)
    return data


def create_car(car_data: Dict) -> Car:
    return Car(
        brand=car_data["brand"],
        fuel_consumption=car_data["fuel_consumption"],
    )


def create_customer(customer_data: Dict) -> Customer:
    return Customer(
        name=customer_data["name"],
        product_cart=customer_data["product_cart"],
        location=customer_data["location"],
        money=customer_data["money"],
        car=create_car(customer_data["car"]),
    )


def create_shop(shop_data: Dict) -> Shop:
    return Shop(
        name=shop_data["name"],
        location=shop_data["location"],
        products=shop_data["products"],
    )


def shop_trip() -> None:
    config_data = extract_config_data()

    fuel_price = config_data["FUEL_PRICE"]

    customers = [
        create_customer(customer) for customer in config_data["customers"]
    ]

    shops = [create_shop(shop) for shop in config_data["shops"]]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        # Calculate trip options as list of (shop, cost) tuples
        trip_options = []
        for shop in shops:
            cost = round(
                customer.calculate_trip_cost(shop.location, fuel_price) * 2
                + shop.calculate_product_cost(customer.product_cart),
                2,
            )
            trip_options.append((shop, cost))

        # Print costs for each shop
        for shop, trip_cost in trip_options:
            print(
                f"{customer.name}'s trip to the {shop.name} costs {trip_cost}",
            )

        # Find affordable shops
        affordable_candidates = [
            (shop, cost) for shop, cost in trip_options
            if cost <= customer.money
        ]
        if affordable_candidates:
            # Find shop with minimum cost
            best_shop, best_cost = min(
                affordable_candidates,
                key=lambda x: x[1]
            )
            print(f"{customer.name} rides to {best_shop.name}\n")
            print(best_shop.give_check(customer))
            print(f"{customer.name} rides home")
            customer.money -= best_cost
            print(f"{customer.name} now has {customer.money} dollars\n")
        else:
            print(
                f"{customer.name} doesn't have enough "
                f"money to make a purchase in any shop",
            )

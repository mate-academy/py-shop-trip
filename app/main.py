import json
import os
import math
from typing import List, Dict, Tuple, Any, Optional

from app.shop import Shop
from app.customer import Customer
from app.car import Car


def calculate_distance(
    location1: List[int],
    location2: List[int]
) -> float:
    return math.sqrt(
        (location1[0] - location2[0]) ** 2 + (location1[1] - location2[1]) ** 2
    )


def calculate_trip_cost(
    customer: Customer,
    shop: Shop,
    fuel_price: float
) -> Tuple[float, float]:
    distance = calculate_distance(
        customer.location,
        shop.location
    )

    fuel_needed = (
        distance / 100
    ) * customer.car.fuel_consumption * 2

    fuel_cost = fuel_needed * fuel_price

    products_cost = sum(
        shop.products[name] * qty
        for name, qty in customer.products.items()
    )

    return fuel_cost + products_cost, products_cost


def shop_trip() -> None:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(current_dir, "config.json")

    with open(config_path, "r") as file:
        data: Dict[str, Any] = json.load(file)

    fuel_price: float = data["FUEL_PRICE"]

    shops: List[Shop] = [
        Shop(shop["name"], shop["location"], shop["products"])
        for shop in data["shops"]
    ]

    customers: List[Customer] = []
    for customer_data in data["customers"]:
        car = Car(
            customer_data["car"]["brand"],
            customer_data["car"]["fuel_consumption"]
        )
        customer = Customer(
            customer_data["name"],
            customer_data["location"],
            customer_data["money"],
            car,
            customer_data["product_cart"]
        )
        customers.append(customer)

    for customer in customers:
        print(f"{customer.name} has {customer.money:g} dollars")

        home_location = customer.location.copy()
        cheapest_shop: Optional[Shop] = None
        min_full_cost = float("inf")
        final_products_cost = 0.0

        for shop in shops:
            full_cost, products_cost = calculate_trip_cost(
                customer, shop, fuel_price
            )

            print(
                f"{customer.name}'s trip to the {shop.name} "
                f"costs {full_cost:.2f}"
            )

            if full_cost < min_full_cost:
                min_full_cost = full_cost
                final_products_cost = products_cost
                cheapest_shop = shop

        if cheapest_shop and customer.money >= min_full_cost:
            print(f"{customer.name} rides to {cheapest_shop.name}")
            print()

            # клієнт їде в магазин
            customer.location = cheapest_shop.location

            cheapest_shop.print_receipt(
                customer,
                customer.products,
                final_products_cost
            )

            print()

            customer.money -= min_full_cost
            customer.location = home_location

            print(f"{customer.name} rides home")

            message = (
                f"{customer.name} now has "
                f"{customer.money:.2f} dollars"
            )
        else:
            message = (
                f"{customer.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )

        print(message)

        if customer != customers[-1]:
            print()

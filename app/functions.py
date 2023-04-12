import json
import math

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def get_dict_from_json() -> dict:
    with open("app/config.json", "r") as data:
        data = json.load(data)

    customers = [Customer(
        name=customer["name"],
        product_cart=customer["product_cart"],
        location=customer["location"],
        money=customer["money"],
        car=Car(brand=customer["car"]["brand"],
                fuel_consumption=customer["car"]["fuel_consumption"], )
    ) for customer in data["customers"]]

    shops = [Shop(
        name=shop["name"],
        products=shop["products"],
        location=shop["location"],
    ) for shop in data["shops"]]

    return {
        "FUEL_PRICE": data["FUEL_PRICE"],
        "customers": customers,
        "shops": shops,
    }


def length_trip_calculation(
        x_point: list[int, int],
        y_point: list[int, int]
) -> float:
    return math.hypot(y_point[0] - x_point[0], y_point[1] - x_point[1])


def cost_trip_calculation(
        length_trip: float,
        fuel_consumption: float,
        fuel_price: float,
        cost_products: float,
) -> float:
    return round(
        length_trip * fuel_consumption / 100
        * fuel_price * 2 + cost_products, 2
    )


def costs_value(shops: list, customer: Customer, products: list) -> dict:
    data = get_dict_from_json()
    costs = {}
    for shop in shops:
        cost_prod = sum(
            [
                shop.products[prod] * customer.product_cart[prod]
                for prod in products
            ]
        )
        costs[shop.get_name] = cost_trip_calculation(
            length_trip=length_trip_calculation(
                shop.location, customer.location
            ),
            fuel_consumption=customer.car.fuel_consumption,
            fuel_price=data["FUEL_PRICE"],
            cost_products=cost_prod)

        print(
            f"{customer.get_name}'s trip to the "
            f"{shop.get_name} costs {costs[shop.get_name]}")

    return costs


def trip(
        costs: dict,
        customer: Customer,
        selected_shop: Shop,
        products: list
) -> None:
    if min(costs.values()) <= customer.get_money:
        current_data = "04/01/2021 12:33:41"

        print(f"{customer.get_name} rides to {selected_shop.get_name}\n")
        print(f"Date: {current_data}")
        print(f"Thanks, {customer.get_name}, for your purchase!")
        print("You have bought: ")
        total_cost = 0
        for prod in products:
            cost = \
                customer.product_cart[prod] * selected_shop.products[prod]
            print(
                f"{customer.product_cart[prod]} {prod}s for "
                f"{cost} dollars")
            total_cost += cost

        print(f"Total cost is {total_cost} dollars")
        print("See you again!\n")
        print(f"{customer.get_name} rides home")
        print(f"{customer.get_name} now has "
              f"{customer.get_money - min(costs.values())} dollars\n")
    else:
        print(f"{customer.get_name} "
              f"doesn't have enough money to make a purchase in any shop")

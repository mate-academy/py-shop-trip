import json
from typing import List
from app.instances.car import Car

from app.instances.customer import Customer
from app.instances.shop import Shop


def file_handler(input_file: str) -> tuple:
    with open(input_file, "r") as file:
        config_data = json.load(file)
        fuel_cost = config_data["FUEL_PRICE"]
    return config_data, fuel_cost


def calculate_trip_distance(customer: Customer, shop: Shop) -> float:
    customer_x, customer_y = customer.location
    shop_x, shop_y = shop.location
    return ((shop_x - customer_x)**2 + (shop_y - customer_y)**2)**0.5


def fuel_cost_one_way(
    customer: Customer,
    fuel_price: float,
    shop: Shop
) -> float:
    return (fuel_price
            * calculate_trip_distance(customer, shop)
            * customer.car.fuel_consumption / 100)


def _products_cost(customer: Customer, shop: Shop) -> float:
    return round(
        sum(shop.products[product] * quantity
            for product, quantity in customer.product_cart.items()), 2
    )


def trip_cost(customer: Customer, fuel_price: float, shop: Shop) -> float:
    return round(fuel_cost_one_way(customer, fuel_price, shop) * 2
                 + _products_cost(customer, shop), 2)


def init_customers(customers_data: dict) -> List[Customer]:
    """ return [
        Customer(**customer, car=Car(**customer["car"]))
        for customer in customers_data["customers"]
     ]"""
    customers = []
    for customer in customers_data["customers"]:
        customers.append(
            Customer
            (
                customer["name"],
                customer["product_cart"],
                customer["location"],
                customer["money"],
                Car(customer["car"]["brand"],
                    customer["car"]["fuel_consumption"])
            )
        )
    return customers


def init_shops(shops_data: dict) -> List[Shop]:
    return [
        Shop(**shop) for shop in shops_data["shops"]
    ]


def visit_shop(
    customers: List[Customer],
    shops: List[Shop],
    fuel_price: float
) -> None:
    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        trips_cost_by_shop = []

        for shop in shops:
            cost = trip_cost(customer, fuel_price, shop)
            print(f"{customer.name}'s trip to the {shop.name} costs {cost}")
            trips_cost_by_shop.append((shop, cost))

        shop, cost = min(trips_cost_by_shop, key=lambda x: x[1])

        if customer.money < cost:
            print(f"{customer.name} doesn't have enough money to make "
                  "a purchase in any shop")
            continue

        fuel_cost = fuel_cost_one_way(customer, fuel_price, shop)
        customer.ride_to_shop(fuel_cost, shop.name, shop.location)

        shop.serve_customer(customer)

        customer.ride_home(fuel_cost)

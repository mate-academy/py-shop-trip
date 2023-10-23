import json
from typing import List, Tuple
from app.car import Car
from app.customer import Customer
from app.shop import Shop


def file_handler(input_file: str) -> dict:
    with open(input_file, "r") as file:
        config_data = json.load(file)
    return config_data


def customer_init(config_data: dict) -> List[Customer]:
    customers = []
    for customer in config_data["customers"]:
        customers.append
        (
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


def shop_init(config_data: dict) -> List[Shop]:
    shops = []
    for shop in config_data["shops"]:
        shops.append
        (
            Shop
            (
                shop["name"],
                shop["location"],
                shop["products"]
            )
        )
    return shops


def calculate_trip_distance(customer: Customer, shop: Shop) -> float:
    customer_x, customer_y = customer["location"]
    shop_x, shop_y = shop["location"]
    return round(((shop_x - customer_x)**2 + (shop_y - customer_y)**2)**5, 2)


def trip_cost(customer: Customer, fuel_price: float, shop: Shop) -> float:
    return round(fuel_price
                 * calculate_trip_distance(customer, shop)
                 * customer.car.fuel_consumption, 2)



import json
from math import sqrt
from app.customer import Customer, Car
from app.shop import Shop


def import_data_from_json() -> tuple:
    with open("app/config.json", "r") as config:
        data_of_file = json.load(config)
        fuel_price = data_of_file["FUEL_PRICE"]

    customers = [
        Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            Car(
                customer["car"]["brand"],
                customer["car"]["fuel_consumption"]
            )
        )
        for customer in data_of_file["customers"]
    ]

    shops = [
        Shop(
            shop["name"],
            shop["location"],
            shop["products"]
        )
        for shop in data_of_file["shops"]
    ]

    return fuel_price, customers, shops


def calculate_distance(
        customer_location: list,
        shop_location: list,
        fuel_price: float,
        car_consume: float
) -> float:
    distance_km = round(
        sqrt(
            (shop_location[0] - customer_location[0])**2
            + (shop_location[1] - customer_location[1])**2
        ), 2
    )
    trip_to_shop = (distance_km / 100) * car_consume * fuel_price * 2
    return trip_to_shop


def calculate_trip_to_shop(customer_cart: dict, shop_products: dict) -> float:
    total_cost = 0

    for product, quantity in customer_cart.items():
        if product in shop_products:
            total_cost += quantity * shop_products[product]

    return total_cost

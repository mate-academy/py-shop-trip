import json
from math import sqrt
from app.customer import Customer
from app.car import Car
from app.shop import Shop


def get_and_transform_data_from_json() -> tuple:
    with open("app/config.json", "r") as file:
        data_from_file = json.load(file)
        fuel_price = data_from_file.get("FUEL_PRICE")
        customers = [
            Customer(
                customer.get("name"),
                customer.get("product_cart"),
                customer.get("location"),
                customer.get("money"),
                Car(
                    customer.get("car").get("brand"),
                    customer.get("car").get("fuel_consumption")
                )
            )
            for customer in data_from_file["customers"]
        ]

        shops = [
            Shop(
                shop.get("name"),
                shop.get("location"),
                shop.get("products")
            )
            for shop in data_from_file["shops"]
        ]
        return fuel_price, customers, shops


def calculate_distance(
        customer_location: list[int],
        shop_location: list[int],
        fuel_price: float,
        fuel_consumption: float) -> float:
    distance_to_shop = sqrt(
        (shop_location[0] - customer_location[0]) ** 2
        + (shop_location[1] - customer_location[1]) ** 2
    )
    trip_to_shop = distance_to_shop / 100 * fuel_consumption * fuel_price * 2

    return round(trip_to_shop, 2)

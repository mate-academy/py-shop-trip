from app.car import Car
from app.customer import Customer
from app.point import Point
from app.shop import Shop


def create_customer(customer: dict) -> Customer:
    return Customer(
        customer["name"],
        get_point(customer["location"]),
        customer["product_cart"],
        customer["money"],
        create_car(customer["car"]),
    )


def get_customers(customers: list[dict]) -> list[Customer]:
    return [
        create_customer(customer)
        for customer in customers
    ]


def create_car(car: dict) -> Car:
    return Car(
        car["brand"],
        car["fuel_consumption"]
    )


def create_shop(shop: dict) -> Shop:
    return Shop(
        shop["name"],
        get_point(shop["location"]),
        shop["products"]
    )


def get_shops(shops: dict) -> list[Shop]:
    return [
        create_shop(shop)
        for shop in shops
    ]


def get_point(point: list[int]) -> Point:
    return Point(point[0], point[1])

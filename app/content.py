import json
from typing import Any

from app.customer import Customer
from app.car import Car
from app.shop import Shop


def get_data_from_file() -> dict[str, Any]:
    with open("app/config.json", "r") as source_file:
        return json.load(source_file)


def get_data_for_trip() -> tuple[int, list[Customer], list[Shop]]:
    data = get_data_from_file()
    fuel_price = data.get("FUEL_PRICE")
    customers = get_customers(data.get("customers"))
    shops = get_shops(data.get("shops"))
    return fuel_price, customers, shops


def get_customers(data: list[dict[str, Any]]) -> list[Customer]:
    return [
        Customer(
            name=customer.get("name"),
            product_cart=customer.get("product_cart"),
            location=customer.get("location"),
            money=customer.get("money"),
            car=Car(
                brand=customer.get("car").get("brand"),
                fuel_consumption=customer.get("car").get("fuel_consumption")
            )
        )
        for customer in data
    ]


def get_shops(data: list[dict[str, Any]]) -> list[Shop]:
    return [
        Shop(
            name=shop.get("name"),
            location=shop.get("location"),
            products=shop.get("products")
        )
        for shop in data
    ]

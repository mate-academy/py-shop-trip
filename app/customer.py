from __future__ import annotations

import math
from typing import Any

from app.shop import Shop


class Customer:
    def __init__(self,
                 name: str,
                 product_cart: dict[str, int],
                 location: list[int],
                 money: int,
                 car: Car
                 ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car


class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption


def create_customer(data: Any) -> list[Customer]:
    customers = []
    for customer in data["customers"]:
        customers.append(Customer(customer["name"],
                                  customer["product_cart"],
                                  customer["location"],
                                  customer["money"],
                                  Car(customer["car"]["brand"],
                                      customer["car"]["fuel_consumption"]
                                      )))
    return customers


def fuel(data: Any) -> float:
    return data["FUEL_PRICE"]


def count_total_fuel_price(customer: Customer, shop: Shop, data: Any) -> float:
    price = fuel(data)

    distance = math.sqrt(((customer.location[0] - shop.location[0]) ** 2)
                         + (customer.location[1] - shop.location[1]) ** 2)
    l_of_fuel = (distance / 100) * customer.car.fuel_consumption

    return (l_of_fuel * price) * 2


def counting_shopping_price(customer: Customer, shop: Shop) -> float:
    price = 0
    for key, value in customer.product_cart.items():
        price += value * shop.products[key]

    return price

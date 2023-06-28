from __future__ import annotations
from dataclasses import dataclass
from app.car import Car


@dataclass()
class Customer:
    name: str
    products: list
    location: list
    money: int
    car: Car

    @classmethod
    def customer_object(cls, customers: list) -> list[Customer]:
        customers_list = []
        for customer in customers:
            customers_list.append(
                Customer(
                    name=customer.get("name"),
                    products=customer.get("product_cart"),
                    location=customer.get("location"),
                    money=customer.get("money"),
                    car=Car.car_object(customer.get("car"))
                )
            )
        return customers_list

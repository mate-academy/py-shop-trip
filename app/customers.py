from __future__ import annotations

from dataclasses import dataclass
from app.car import Car
from app.data import data


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: list[int]
    money: int
    car: Car

    def print_customers_money(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    @staticmethod
    def create_customers() -> list[Customer]:
        customers_list = []
        for customer in data.get("customers"):
            customers_list.append(
                Customer(
                    name=customer.get("name"),
                    product_cart=customer.get("product_cart"),
                    location=customer.get("location"),
                    money=customer.get("money"),
                    car=Car(customer.get("car").get("brand"),
                            customer.get("car").get("fuel_consumption"),
                            fuel_price=data.get("FUEL_PRICE"))
                )
            )
        return customers_list

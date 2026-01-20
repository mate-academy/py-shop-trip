from __future__ import annotations
from app.car import Car


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: float,
            car: Car
    ) -> None:
        self.money = money
        self.location = location
        self.product_cart = product_cart
        self.name = name
        self.car = car
        self.home_location = location

    def get_money(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def __repr__(self) -> str:
        return self.name

    @classmethod
    def create_customers(cls, data: dict) -> list[Customer]:
        """Create Customer instances from the provided data."""
        customers = []
        for customer_data in data["customers"]:
            car_data = customer_data["car"]
            car = Car(**car_data)

            customers.append(
                cls(
                    name=customer_data["name"],
                    product_cart=customer_data["product_cart"],
                    location=customer_data["location"],
                    money=customer_data["money"],
                    car=car
                )
            )
        return customers

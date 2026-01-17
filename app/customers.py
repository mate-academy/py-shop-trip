from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Dict, List


@dataclass
class Customers:
    name: str
    product_cart: Dict[str, int]
    location: List[int]
    money: int | float
    car_brand: str
    fuel_consumption: float | int
    fuel_price: int | float

    @classmethod
    def from_file_data(
            cls,
            file_data: Dict[str, Any],
            fuel_price: float) -> Customers:

        return cls(
            name=file_data["name"],
            product_cart=file_data["product_cart"],
            location=file_data["location"],
            money=file_data["money"],
            car_brand=file_data["car"]["brand"],
            fuel_consumption=file_data["car"]["fuel_consumption"],
            fuel_price=fuel_price
        )

    @classmethod
    def load_person(
            cls,
            customer_data: List[Dict[str, Any]],
            fuel_price: float) -> list[Customers]:

        customers = []
        for data in customer_data:
            customer = cls.from_file_data(data, fuel_price)
            customers.append(customer)
        return customers

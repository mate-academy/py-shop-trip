import dataclasses
from typing import List

from app.car import Car


@dataclasses.dataclass
class Customer:
    name: str
    product_cart: dict
    car: Car
    money: int

    @classmethod
    def list_read(cls, list_customers: List[dict]) -> list:
        customers_list = []
        for customer in list_customers:
            customers_list.append(
                Customer(
                    name=customer["name"],
                    product_cart=customer["product_cart"],
                    money=customer["money"],
                    car=Car(
                        brand=customer["car"]["brand"],
                        fuel_consumption=customer["car"]["fuel_consumption"],
                        location=customer["location"]
                    )
                )
            )
        return customers_list

from dataclasses import dataclass

from app.car import Car


@dataclass
class Customer:
    name: str
    product_cart: dict
    money: int
    car: Car

    def __repr__(self) -> str:
        return self.name

    @classmethod
    def constructor(cls, customer_list: list) -> list:
        for index, customer in enumerate(customer_list):
            customer_list[index] = Customer(
                name=customer["name"],
                product_cart=customer["product_cart"],
                money=customer["money"],
                car=Car(
                    brand=customer["car"]["brand"],
                    fuel_consumption=customer["car"]["fuel_consumption"],
                    location=customer["location"]
                )
            )
        return customer_list

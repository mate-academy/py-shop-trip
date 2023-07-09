from dataclasses import dataclass

from app.car import Car


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: list[int, int]
    money: int
    car: Car

    def count_money(self) -> None:
        print(f"{self.name} has {self.money} dollars")


def customer_from_dict(dictionary: dict) -> Customer:
    return Customer(dictionary["name"],
                    dictionary["product_cart"],
                    dictionary["location"],
                    dictionary["money"],
                    Car(dictionary["car"]["brand"],
                        dictionary["car"]["fuel_consumption"]))

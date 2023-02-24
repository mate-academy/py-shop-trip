import dataclasses
import datetime
from typing import List, Any

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

    def make_purchase(self, best_shop: Any) -> None:
        print(f"{self.name} rides to {best_shop.name}\n")
        print(
            f"Date: "
            f"{datetime.datetime.now().strftime(f'%d/%m/%Y %H:%M:%S')}"
        )
        print(f"Thanks, {self.name}, for you purchase!\nYou have bought: ")

        best_shop.buy_product(self.product_cart)

        print(
            f"{self.name} rides home\n"
            f"{self.name} now has {self.money} dollars\n"
        )

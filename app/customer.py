from math import sqrt
import datetime
from typing import Dict, Any


class Customer:

    def __init__(
            self, name: str,
            product_cart: Dict[str, Any],
            location: tuple,
            money: float, car: Any
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    @staticmethod
    def calculate_distance(location1: tuple, location2: tuple) -> float:
        delta_x = location1[0] - location2[0]
        delta_y = location1[1] - location2[1]
        distance = sqrt(delta_x ** 2 + delta_y ** 2)
        return distance

    def purchase_receipt(
            self, shop_name: str,
            products: Dict[str, float]
    ) -> None:
        current_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        print(
            f"\nDate: {current_time}\nThanks, "
            f"{self.name}, "
            f"for your purchase!\nYou have bought:"
        )

        total_cost = 0
        for item, quantity in self.product_cart.items():

            cost = products[item] * quantity
            total_cost += cost
            cost = int(cost) if cost == int(cost) else round(cost, 1)
            print(f"{quantity} {item}s for {cost} dollars")

        print(f"Total cost is {total_cost:.1f} dollars\nSee you again!\n")

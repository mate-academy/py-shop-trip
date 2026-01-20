from datetime import datetime
from typing import Dict, Tuple
from app.car import Car


class Customer:
    def __init__(self, name: str, location: Tuple[int, int], money: float,
                 product_cart: Dict[str, int], car: Car) -> None:
        self.name = name
        self.home = location
        self.location = location
        self.money = money
        self.product_cart = product_cart
        self.car = car

    def distance_to(self, point: Tuple[int, int]) -> float:
        return ((self.location[0] - point[0])**2
                + (self.location[1] - point[1])**2) ** 0.5

    def ride_to(self, destination: Tuple[int, int]) -> None:
        self.location = destination

    def ride_home(self) -> None:
        self.location = self.home

    def purchase(self, shop_name: str, product_prices: Dict[str, float]) -> float:
        date_str = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
        print(f"\nDate: {date_str}")
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought:")

        total_cost = 0
        for item, qty in self.product_cart.items():
            cost = qty * product_prices[item]
            total_cost += cost
            # Format numbers to match expected output
            if cost == int(cost):
                cost_str = f"{int(cost)}"
            elif cost * 10 == int(cost * 10):  # One decimal place
                cost_str = f"{cost:.1f}"
            else:
                cost_str = f"{cost:.2f}".rstrip("0").rstrip(".")
            print(f"{qty} {item}s for {cost_str} dollars")

        # Format total cost to match expected output
        if total_cost == int(total_cost):
            total_str = f"{int(total_cost)}"
        elif total_cost * 10 == int(total_cost * 10):  # One decimal place
            total_str = f"{total_cost:.1f}"
        else:
            total_str = f"{total_cost:.2f}".rstrip("0").rstrip(".")
        print(f"Total cost is {total_str} dollars")
        print("See you again!")

        self.money -= total_cost
        return total_cost

import datetime
import math

from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(self,
                 name: str,
                 product_cart: dict,
                 location: list,
                 money: int,
                 car: dict) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(car["brand"], car["fuel_consumption"])

    def total_cost_calculation(self, shop: Shop, fuel_price: float) -> float:
        x_offset, y_offset = [shop.location[0] - self.location[0],
                              shop.location[1] - self.location[1]]
        distance = math.hypot(x_offset, y_offset)

        total_cost = round(
            self.car.fuel_consumption * distance / 100.0 * fuel_price * 2, 2
        )
        total_cost += sum(
            shop.products[product] * count
            for product, count in self.product_cart.items()
        )
        print(f"{self.name}'s trip to the {shop.name} costs {total_cost}")

        return total_cost

    def shopping(self, shop: Shop, shopping_cost: float) -> None:
        current_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print("Date:", current_time)
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought: ")

        total = 0
        for product, count in self.product_cart.items():
            cost = round(shop.products[product] * count, 2)
            print(f"{count} {product}s for {cost} dollars")
            total += cost

        total = round(total, 2)
        print(f"Total cost is {total} dollars")

        self.money -= shopping_cost

        print("See you again!\n")
        print(f"{self.name} rides home")
        print(f"{self.name} now has {self.money} dollars\n")

    def __str__(self) -> str:
        return f"{self.name} has {self.money} dollars"

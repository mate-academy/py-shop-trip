import datetime

from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(self,
                 name: str,
                 product_cart: dict[str: int],
                 location: list[int],
                 money: int,
                 car: dict[str: str | float]) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(car["brand"], car["fuel_consumption"])

    def calculate_total_cost(self, shop: Shop, fuel_price: float) -> float:
        offset = [shop.location[0] - self.location[0],
                  shop.location[1] - self.location[1]]
        distance = (offset[0] ** 2 + offset[1] ** 2) ** 0.5

        total_cost = round(self.car.fuel_consumption * distance / 100
                           * fuel_price * 2, 2)

        for product, count in self.product_cart.items():
            total_cost += shop.products[product] * count

        total_cost = round(total_cost, 2)

        print(f"{self.name}'s trip to the {shop.name} costs {total_cost}")

        return total_cost

    def go_to_shopping(self, shop: Shop, shopping_cost: float) -> None:
        print("Date: " + datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought: ")

        total = 0
        for product, count in self.product_cart.items():
            cost = round(shop.products[product] * count, 2)
            print(f"{count} {product}s for {cost} dollars")
            total += cost

        print(f"Total cost is {round(total, 2)} dollars")

        self.money -= shopping_cost

        print("See you again!\n")
        print(f"{self.name} rides home")
        print(f"{self.name} now has {self.money} dollars\n")

    def __str__(self) -> str:
        return f"{self.name} has {self.money} dollars"

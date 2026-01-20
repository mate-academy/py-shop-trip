import datetime
import math

from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list[int],
            money: int,
            car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def money_(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def calculate_road(self, shop: Shop, fuel_cost: float) -> float:
        distance = math.dist(self.location, shop.location)
        return distance * (self.car.fuel_consumption / 100) * fuel_cost

    def cost_shop(self, shopping_price: dict) -> None:
        for product, amount in self.product_cart.items():
            price = (amount * shopping_price[product])
            print(f"{amount} {product}s for {price} dollars")

    def cost_of_product(self, shop: Shop) -> float:
        total_expanse = sum(
            [
                price * int(self.product_cart.get(product))
                for product, price in shop.products.items()
            ]
        )

        return total_expanse

    def bill(self, shops: list[Shop], fuel_cost: float) -> None:
        cheapest = {}

        for shop in shops:
            spent_for_shopping = round((self.calculate_road(
                shop, fuel_cost
            )) * 2 + self.cost_of_product(shop), 2)

            print(f"{self.name}'s trip to the {shop.name} "
                  f"costs {spent_for_shopping}")

            cheapest[shop] = spent_for_shopping

        if len(cheapest) != 0 and max(
                cheapest.values()
        ) < self.money:
            chosen_shop = min(cheapest, key=cheapest.get)
            print(f"{self.name} rides to {chosen_shop.name}\n")

            self.money -= float(cheapest[chosen_shop])

            data = datetime.datetime.now().strftime("%d/%m/20%y %H:%M:%S")
            print(f"Date: {data}\nThanks, {self.name}, "
                  f"for your purchase!\nYou have bought: ")
            self.cost_shop(chosen_shop.products)
            print(f"Total cost is {self.cost_of_product(chosen_shop)} "
                  f"dollars\n"
                  f"See you again!\n\n{self.name} rides home\n"
                  f"{self.name} now has {round(self.money, 2)} dollars\n")
        else:
            print(f"{self.name} doesn't have enough money "
                  f"to make a purchase in any shop")

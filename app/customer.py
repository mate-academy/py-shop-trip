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

    def has_money(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def cost_per_km(self) -> float:
        return self.car.fuel_consumption / 100

    def calculate_road_expenses(self, shops: Shop, fuel_cost: float) -> float:
        distance = math.dist(self.location, shops.location)
        return distance * self.cost_per_km() * fuel_cost

    def cost_by_category(self, shopping_price: dict) -> None:
        for product, amount in self.product_cart.items():
            price = (amount * shopping_price[product])
            print(f"{amount} {product}s for {price} dollars")

    def product_cost(self, shops: Shop) -> float:
        total_expanse = sum(
            [
                price * int(self.product_cart.get(product))
                for product, price in shops.products.items()
            ]
        )

        return total_expanse

    def bill_by_shop(self, shops: list[Shop], fuel_cost: float) -> None:
        cheapest_shop = {}

        for shop in shops:
            spent_for_shopping = round((self.calculate_road_expenses(
                shop, fuel_cost
            )) * 2 + self.product_cost(shop), 2)

            print(f"{self.name}'s trip to the {shop.name} "
                  f"costs {spent_for_shopping}")

            cheapest_shop[shop] = spent_for_shopping

        if len(cheapest_shop) != 0 and max(
                cheapest_shop.values()
        ) < self.money:
            chosen_shop = min(cheapest_shop, key=cheapest_shop.get)
            print(f"{self.name} rides to {chosen_shop.name}\n")

            self.money -= float(cheapest_shop[chosen_shop])

            data = datetime.datetime.now().strftime("%d/%m/20%y %H:%M:%S")
            print(f"Date: {data}")
            print(f"Thanks, {self.name}, for your purchase!")
            print("You have bought: ")
            self.cost_by_category(chosen_shop.products)
            print(f"Total cost is {self.product_cost(chosen_shop)} dollars")
            print("See you again!\n")
            print(f"{self.name} rides home")
            print(f"{self.name} now has {round(self.money, 2)} dollars\n")
        else:
            print(f"{self.name} doesn't have enough money "
                  f"to make a purchase in any shop")

import datetime
import math
from typing import List, Dict, Optional
from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: Dict[str, int],
            location: List[int],
            money: int,
            car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def money_of_costomer(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def cost_per_km(self) -> float:
        return self.car.fuel_consumption / 100

    def calculate_road_expenses(self, shop: Shop, fuel_cost: float) -> float:
        distance = math.dist(self.location, shop.location)
        return distance * self.cost_per_km() * fuel_cost

    def cost_of_category(self, shopping_price: dict) -> None:
        for product, amount in self.product_cart.items():
            price = (amount * shopping_price[product])
            print(f"{amount} {product}s for {price} dollars")

    def product_cost(self, shop: Shop) -> float:
        total_expanse = sum(
            [
                price * int(self.product_cart.get(product))
                for product, price in shop.products.items()
            ]
        )

        return total_expanse

    def calculate_total_costs(self, shops: List[Shop], fuel_cost: float) -> Dict[Shop, float]:
        total_costs = {}
        for shop in shops:
            spent_for_shopping = round((self.calculate_road_expenses(shop, fuel_cost)) * 2 + self.product_cost(shop), 2)
            total_costs[shop] = spent_for_shopping
        return total_costs

    def print_trip_costs(self, total_costs: Dict[Shop, float]) -> None:
        for shop, cost in total_costs.items():
            print(f"{self.name}'s trip to the {shop.name} costs {cost}")

    def find_cheapest_shop(self, total_costs: Dict[Shop, float]) -> Optional[Shop]:
        if len(total_costs) != 0 and max(total_costs.values()) < self.money:
            return min(total_costs, key=total_costs.get)
        return None

    def finalize_purchase(self, chosen_shop: Shop, total_cost: float) -> None:
        self.money -= float(total_cost)

        data = datetime.datetime.now().strftime("%d/%m/20%y %H:%M:%S")
        print(f"Date: {data}\nThanks, {self.name}, for your purchase!\nYou have bought: ")
        self.cost_of_category(chosen_shop.products)
        print(f"Total cost is {self.product_cost(chosen_shop)} dollars\n"
              f"See you again!\n\n{self.name} rides home\n"
              f"{self.name} now has {round(self.money, 2)} dollars\n")

    def bill_by_shop(self, shops: List[Shop], fuel_cost: float) -> None:
        total_costs = self.calculate_total_costs(shops, fuel_cost)
        self.print_trip_costs(total_costs)
        chosen_shop = self.find_cheapest_shop(total_costs)

        if chosen_shop:
            print(f"{self.name} rides to {chosen_shop.name}\n")
            self.finalize_purchase(chosen_shop, total_costs[chosen_shop])
        else:
            print(f"{self.name} doesn't have enough money to make a purchase in any shop")

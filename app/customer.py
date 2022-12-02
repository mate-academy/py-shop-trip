from typing import List

from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: int | float,
            car: dict
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(car["brand"], car["fuel_consumption"])

    def total_cost_per_shop(
            self,
            car: Car,
            shop: Shop,
            fuel_price: float
    ) -> float:
        total_cost_per_shop = round(car.fuel_cost(self, shop, fuel_price)
                                    * 2 + shop.products_price(self), 2)
        return total_cost_per_shop

    def shop_to_go(
            self,
            car: Car,
            shops: List[Shop],
            fuel_price: float
    ) -> Shop | None:
        print(f"{self.name} has {self.money} dollars")

        shop_costs = {}

        for shop in shops:
            total_cost = self.total_cost_per_shop(car, shop, fuel_price)
            shop_costs[shop] = total_cost
            print(f"{self.name}'s trip "
                  f"to the {shop.name} costs {total_cost}")

        cheapest_travel_shop = min(shop_costs, key=shop_costs.get)

        if self.money < shop_costs[cheapest_travel_shop]:
            print(f"{self.name} doesn't have enough money "
                  f"to make purchase in any shop")
            return
        print(f"{self.name} rides to {cheapest_travel_shop.name}" + "\n")

        return cheapest_travel_shop

    def customer_rides_home(
            self,
            car: Car,
            shop: Shop,
            fuel_price: float
    ) -> None:
        balance = self.money - self.total_cost_per_shop(car, shop, fuel_price)
        print(f"{self.name} rides home\n"
              f"{self.name} now has {balance} dollars\n")

import math
from datetime import datetime

from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(self, customer_info: dict) -> None:
        self.name: str = customer_info["name"]
        self.product_cart: dict = customer_info["product_cart"]
        self.location: list[int] = customer_info["location"]
        self.money: int | float = customer_info["money"]
        self.car: Car = Car(
            customer_info["car"]["brand"],
            customer_info["car"]["fuel_consumption"]
        )

    def select_shop(
            self, shops: list[Shop], fuel_price: int | float
    ) -> bool:
        print(f"{self.name} has {self.money} dollars")

        trips_costs: dict[int: Shop] = {}
        for shop in shops:
            products_cost = self._calculate_product_costs(shop)
            fuel_cost = self._calculate_fuel_costs(shop, fuel_price)
            trip_cost = products_cost + fuel_cost
            print(f"{self.name}'s trip to the {shop.name} costs {trip_cost}")
            trips_costs[trip_cost] = shop

        cheapest_trip_cost = min(trips_costs.keys())
        if self.money < cheapest_trip_cost:
            print(f"{self.name} doesn't have enough "
                  f"money to make purchase in any shop")
            return False
        else:
            self._selected_shop = trips_costs[cheapest_trip_cost]
            self.money -= cheapest_trip_cost
            print(f"{self.name} rides to {self._selected_shop.name}\n")
            return True

    def make_purchases(self) -> None:
        date = datetime(2021, 4, 1, 12, 33, 41).strftime("%m/%d/%Y %H:%M:%S")
        print(f"Date: {date}")
        print(f"Thanks, {self.name}, for you purchase!")

        print("You have bought: ")
        total_costs = 0
        for product, number in self.product_cart.items():
            price = self._selected_shop.assortment[product] * number
            print(f"{number} {product}s for {price} dollars")
            total_costs += price

        print(f"Total cost is {total_costs} dollars")
        print("See you again!\n")

    def go_home(self) -> None:
        print(f"{self.name} rides home")
        print(f"{self.name} now has {self.money} dollars\n")

    def _calculate_fuel_costs(self, shop: Shop, fuel_price: float) -> float:
        distance = math.dist(self.location, shop.location)
        fuel_consumption = self.car.fuel_consumption / 100
        fuel_consumption_factor = 2

        return round(
            fuel_consumption_factor * distance
            * (fuel_consumption * fuel_price), 2
        )

    def _calculate_product_costs(self, shop: Shop) -> int:
        return sum(
            [
                number * price for number, price
                in zip(self.product_cart.values(), shop.assortment.values())
            ]
        )

from typing import List, Union
from math import dist

from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(self,
                 name: str,
                 product_cart: dict,
                 location: List[int],
                 money: float,
                 car: Car,
                 fuel_price: float) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car
        self.fuel_price = fuel_price

    def __calculate_trip_cost(self, shop: Shop) -> float:
        fuel_cost = dist(self.location, shop.location) / 100 * (
            self.car.fuel_consumption * self.fuel_price)

        products_cost = sum(
            shop.products[product] * self.product_cart[product]
            for product in shop.products
        )

        return round(2 * fuel_cost + products_cost, 2)

    def pick_shop(self, shops: List[Shop]) -> Union[Shop, None]:
        min_cost = self.money
        trip_cost = 0
        cheapest_shop = shops[0]

        print(f"{self.name} has {self.money} dollars")

        for shop in shops:
            trip_cost = self.__calculate_trip_cost(shop)
            print(f"{self.name}'s trip to the {shop.name} "
                  f"costs {trip_cost}")
            if trip_cost < min_cost:
                min_cost = trip_cost
                cheapest_shop = shop

        if trip_cost > self.money:
            print(f"{self.name} doesn't have enough money "
                  f"to make a purchase in any shop")
            return None
        else:
            print(f"{self.name} rides to {cheapest_shop.name}\n")

        return cheapest_shop

    def go_home(self, cheapest_shop: Shop) -> None:
        print(f"{self.name} rides home")
        print(f"{self.name} now has "
              f"{self.money - self.__calculate_trip_cost(cheapest_shop)}"
              f" dollars\n")

from math import sqrt
from typing import Dict, List
from app.shop import Shop


class Customer:
    def __init__(self,
                 name: str,
                 products_cart: Dict,
                 location: List[int],
                 money: int,
                 car: Dict) -> None:
        self.name = name
        self.products_cart = products_cart
        self.location = location
        self.money = money
        self.car = car

    def start_balance(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def get_product_cost(self, shop: Shop) -> float:
        return sum(
            price * int(self.products_cart.get(product))
            for product, price in shop.products.items()
        )

    def calculated_distance_to_shop(self, shop: Shop) -> float:
        distance = sqrt(
            (shop.location[0] - self.location[0]) ** 2
            + (shop.location[1] - self.location[1]) ** 2
        )
        return distance

    def calculated_fuel_cost(self, fuel_price: float, shop: Shop) -> float:
        fuel_cost = (((self.car["fuel_consumption"]
                     * self.calculated_distance_to_shop(shop)
                     / 100) * fuel_price) * 2)

        return fuel_cost

    def get_trip_cost(self, fuel_price: float, shops: List[Shop]) -> dict:
        dict_with_trip = {}
        for shop in shops:
            trip_cost = round(self.calculated_fuel_cost(fuel_price, shop)
                              + self.get_product_cost(shop), 2)
            dict_with_trip[trip_cost] = shop.name
            print(f"{self.name}'s trip to the {shop.name} costs {trip_cost}")

        return dict_with_trip

    def select_cheapest_trip(self, trips: Dict) -> str:
        cheapest_trip = min(trips)
        shop_name = None
        if cheapest_trip < self.money:
            self.money -= cheapest_trip
            shop_name = trips[cheapest_trip]
            print(f"{self.name} rides to {shop_name}" + "\n")
        else:
            print(f"{self.name} doesn't have enough money "
                  f"to make a purchase in any shop")
        return shop_name

    def ride_home_and_calculated_money(self) -> None:
        print(f"{self.name} rides home")
        print(f"{self.name} now has {self.money} dollars" + "\n")

from app.shop import Shop
from app.car import Car
import math


class Customer:
    def __init__(self,
                 name: str,
                 product_cart: dict,
                 location: list,
                 money: int,
                 car: Car) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

        self.home_location = self.location

    def distance(self, location: list) -> float:
        x1, y1 = self.location
        x2, y2 = location
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def trip_prices(self, shops: list[Shop]) -> dict:
        return {round(2 * self.car.gas_price(self.distance(shop.location))
                      + shop.total_product_price(self.product_cart), 2): shop
                for shop in shops}

    def choose_minimal_cost_trip(self, shops_with_prices: dict) -> Shop | None:
        if all(key > self.money for key in shops_with_prices.keys()):
            return None
        return shops_with_prices[min(key for key in shops_with_prices.keys()
                                     if self.money >= key)]

    def show_trips_info(self, trips: dict) -> None:
        for cost, shop in trips.items():
            print(f"{self.name}'s trip to the {shop.name} costs {cost}")

    def drive_to(self, location: list[int]) -> None:
        self.money -= self.car.gas_price(self.distance(location))
        self.location = location

    def go_to_shop(self, shops: list[Shop]) -> None:
        trips = self.trip_prices(shops)
        print(f"{self.name} has {self.money} dollars")
        self.show_trips_info(trips)

        lowest_price_shop = self.choose_minimal_cost_trip(trips)
        if not lowest_price_shop:
            print(f"{self.name} doesn't have enough money "
                  f"to make purchase in any shop")
            return

        self.drive_to(lowest_price_shop.location)
        print(f"{self.name} rides to {lowest_price_shop.name}\n")
        self.money -= lowest_price_shop.sell(self.product_cart, self.name)

        print(f"{self.name} rides home")
        self.drive_to(self.home_location)

        print(f"{self.name} now has {round(self.money, 2)} dollars\n")

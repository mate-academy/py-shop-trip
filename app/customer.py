from __future__ import annotations
import datetime
from dataclasses import dataclass
from app.car import Car, Location
from app.shop import Shop


@dataclass
class Customer:
    name: str
    product_cart: dict
    home_location: Location
    current_location: Location
    money: int | float
    car: Car

    def __repr__(self) -> str:
        return self.name

    def calculate_fuel_cost(self,
                            fuel_price: float,
                            target_loc: Location) -> float:
        distance = (((self.home_location.x_ - target_loc.x_) ** 2
                     + (self.home_location.y_ - target_loc.y_) ** 2) ** 0.5)
        consumed_fuel = distance * (self.car.fuel_consumption / 100)
        fuel_cost = 2 * consumed_fuel * fuel_price
        return round(fuel_cost, 2)

    def calculate_products_price(self, shop: Shop) -> int | float:
        return sum(self.product_cart[prod]
                   * shop.products[prod] for prod in shop.products.keys())

    def calculate_trip_cost(self, shop: Shop, fuel_price: float) -> float:
        total_trip_cost = (self.calculate_fuel_cost(fuel_price, shop.location)
                           + self.calculate_products_price(shop))
        return total_trip_cost

    def plan_trip(self,
                  shop_list: list[Shop],
                  fuel_price: float) -> Shop | None:
        print(f"{self.name} has {self.money} dollars")
        cheapest_shop = None
        for shop in shop_list:
            trip_cost = self.calculate_trip_cost(shop, fuel_price)
            print(f"{self.name}'s trip to the {shop.name} costs {trip_cost}")
            if cheapest_shop is None:
                cheapest_shop = shop
            if trip_cost < self.calculate_trip_cost(cheapest_shop,
                                                    fuel_price):
                cheapest_shop = shop
        if self.calculate_trip_cost(cheapest_shop,
                                    fuel_price) < self.money:
            print(f"{self.name} rides to {cheapest_shop}")
            return cheapest_shop
        else:
            print(f"{self.name} doesn't have enough "
                  f"money to make a purchase in any shop")

    def shopping(self, shop: Shop) -> None:
        self.current_location = shop.location
        print(f"\nDate: "
              f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {self.name}, for your purchase!\nYou have bought: ")
        for prod in shop.products:
            price = shop.products[prod] * self.product_cart[prod]
            print(f"{self.product_cart[prod]} {prod}s for {price} dollars")
        print(f"Total cost is {self.calculate_products_price(shop)} dollars")
        print("See you again!\n")

    def go_home(self, shop: Shop, fuel_price: float) -> None:
        self.current_location = self.home_location
        print(f"{self.name} rides home")
        self.money -= self.calculate_trip_cost(shop, fuel_price)
        print(f"{self.name} now has {self.money} dollars\n")

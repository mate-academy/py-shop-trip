from __future__ import annotations
import datetime
from dataclasses import dataclass
from app.car import Car, Location
from app.shop import Shop, Product


@dataclass
class Customer:
    name: str
    product_cart: list[Product]
    home_location: Location
    current_location: Location
    money: int | float
    car: Car
    cheapest_shop: Shop = None

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
        total_cost = 0
        for product_from_cart in self.product_cart:
            for product_in_shop in shop.products:
                if product_from_cart.name == product_in_shop.name:
                    total_cost += (product_from_cart.quantity
                                   * product_in_shop.price)
        return total_cost

    def calculate_trip_cost(self, shop: Shop, fuel_price: float) -> float:
        total_trip_cost = (self.calculate_fuel_cost(fuel_price, shop.location)
                           + self.calculate_products_price(shop))
        return total_trip_cost

    def plan_trip(self,
                  shop_list: list[Shop],
                  fuel_price: float) -> Shop | None:
        print(f"{self.name} has {self.money} dollars")
        for shop in shop_list:
            trip_cost = self.calculate_trip_cost(shop, fuel_price)
            print(f"{self.name}'s trip to the {shop.name} costs {trip_cost}")
            if self.cheapest_shop is None:
                self.cheapest_shop = shop
            if trip_cost < self.calculate_trip_cost(self.cheapest_shop,
                                                    fuel_price):
                self.cheapest_shop = shop
        if self.calculate_trip_cost(self.cheapest_shop,
                                    fuel_price) < self.money:
            print(f"{self.name} rides to {self.cheapest_shop}")
            return self.cheapest_shop
        else:
            print(f"{self.name} doesn't have enough "
                  f"money to make a purchase in any shop")
            return

    def shopping(self, shop: Shop) -> None:
        self.current_location = shop.location
        print(f"\nDate: "
              f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {self.name}, for your purchase!\nYou have bought: ")
        for cart_product in self.product_cart:
            for shop_product in shop.products:
                if cart_product.name == shop_product.name:
                    print(f"{cart_product.quantity} {cart_product.name}s for "
                          f"{(cart_product.quantity * shop_product.price)} "
                          f"dollars")
        print(f"Total cost is {self.calculate_products_price(shop)} dollars")
        print("See you again!\n")

    def go_home(self, shop: Shop, fuel_price: float) -> None:
        self.current_location = self.home_location
        print(f"{self.name} rides home")
        self.money = self.money - self.calculate_trip_cost(shop, fuel_price)
        print(f"{self.name} now has {self.money} dollars\n")

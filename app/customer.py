from __future__ import annotations
import math

from app.car import Car


class Customer:
    def __init__(self, customers: dict) -> None:
        self.name = customers["name"]
        self.product_cart = customers["product_cart"]
        self.location = customers["location"]
        self.money = customers["money"]
        self.car = customers["car"]
        self.best_shop = None
        self.best_price = None

    def calculate_distance_to_shop(self, other: Customer) -> float:
        new_x = self.location[0] - other.location[0]
        new_y = self.location[-1] - other.location[-1]
        return math.sqrt(new_x ** 2 + new_y ** 2)

    def choose_shop(self, shops: list, fuel_price: float | int) -> None:
        car = Car(self.car)
        good_shops = []
        for shop in shops:
            product_cost = shop.calculate_cost(self.product_cart)
            distance = self.calculate_distance_to_shop(shop)
            trip_cost = car.fuel_cost(distance, fuel_price) * 2
            total_cost = round(trip_cost + product_cost, 2)

            print(f"{self.name}'s trip to the "
                  f"{shop.name} costs {total_cost}")
            if self.money > total_cost:
                good_shops.append((shop, total_cost))

        if good_shops:
            best_shop, best_price = sorted(good_shops, key=lambda a: a[1])[0]
            print(f"{self.name} rides to {best_shop.name}\n")
            self.best_shop = best_shop
            self.best_price = best_price
        else:
            print(f"{self.name} doesn't have enough money "
                  f"to make purchase in any shop")

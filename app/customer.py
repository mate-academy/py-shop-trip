from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.shop import Shop

from app.car import Car

import dataclasses


@dataclasses.dataclass
class Customer:
    name: str
    product_cart: dict
    location: list[int]
    money: float
    car: Car

    @staticmethod
    def create_customers(customers: dict) -> list[Customer]:
        customers_list = []
        for customer in customers:
            customers_list.append(
                Customer(
                    customer["name"],
                    customer["product_cart"],
                    customer["location"],
                    customer["money"],
                    Car(
                        customer["car"]["brand"],
                        customer["car"]["fuel_consumption"]
                    )
                )
            )
        return customers_list

    def print_money_remainder(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def ride_home_and_show_remainder(self) -> None:
        print(
            f"{self.name} rides home\n"
            f"{self.name} now has {round(self.money, 2)} dollars\n"
        )

    def to_shop_distance(self, shop: Shop) -> float:
        x1, y1 = self.location
        x2, y2 = shop.shop_location
        result = (((x2 - x1) ** 2) + ((y1 - y2) ** 2)) ** 0.5
        return result

    def trip_cost(self, shop: Shop, fuel_price: float) -> float:
        distance = self.to_shop_distance(shop)
        one_km_consumption = self.car.fuel_consumption / 100
        consumption_for_trip = distance * one_km_consumption
        final_cost = consumption_for_trip * fuel_price
        return final_cost

    def charge_for_trip(self, shop: Shop, fuel_price: float) -> callable:
        self.money -= float(self.trip_cost(shop, fuel_price)) * 2

    def choose_ideal_shop(self, shops: list, fuel_price: float) -> Shop | None:
        comparison_dict = {}
        for shop in shops:
            travel_cost = self.trip_cost(shop, fuel_price) * 2
            products_cost = sum(
                self.product_cart[product] * shop.shop_prices[product]
                for product in self.product_cart.keys()
            )
            total_cost = round(travel_cost + products_cost, 2)
            comparison_dict[total_cost] = shop
            print(
                f"{self.name}'s trip to "
                f"the {shop.shop_name} costs {total_cost}"
            )
        suitable_cost = min(comparison_dict)
        if self.money < suitable_cost:
            print(f"{self.name} doesn't have enough "
                  f"money to make purchase in any shop")
        else:
            shop_to_ride = comparison_dict[suitable_cost]
            print(f"{self.name} rides to {shop_to_ride.shop_name}\n")
            return shop_to_ride

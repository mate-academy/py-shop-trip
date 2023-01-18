from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            products_to_buy: dict,
            location: list[int],
            money: float,
            car: Car
    ) -> None:
        self.name = name
        self.products_to_buy = products_to_buy
        self.location = location
        self.money = money
        self.car = car

    @staticmethod
    def create_customers(json_input: dict) -> list[Customer]:
        customers_list = []
        for customer in json_input["customers"]:
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
        x1 = self.location[0]
        y1 = self.location[1]
        x2 = shop.location[0]
        y2 = shop.location[1]
        result = (((x2 - x1) ** 2) + ((y1 - y2) ** 2)) ** 0.5
        return result

    def cost_drive_to_shop(self, shop: Shop, fuel_price: float) -> float:
        distance = self.to_shop_distance(shop)
        one_km_consumption = self.car.fuel_consumption / 100
        consumption_for_trip = distance * one_km_consumption
        final_cost = consumption_for_trip * fuel_price
        return final_cost

    def charge_for_trip(self, shop: Shop, fuel_price: float) -> callable:
        self.money -= float(self.cost_drive_to_shop(shop, fuel_price)) * 2

    def check_shops_products(self, shop: Shop) -> bool:
        for product in self.products_to_buy:
            if product not in shop.products_provides:
                print(f"Shop {shop.name} doesn't provides {product}")
                return False
            return True

    def choose_shop(self, shops: list, fuel_price: float) -> Shop | None:
        comparison_dict = {}
        for shop in shops:
            if not self.check_shops_products(shop):
                continue
            travel_cost = self.cost_drive_to_shop(shop, fuel_price) * 2
            products_cost = sum(
                self.products_to_buy[product] * shop.products_provides[product]
                for product in self.products_to_buy.keys()
            )
            total_cost = round(travel_cost + products_cost, 2)
            comparison_dict[total_cost] = shop
            print(
                f"{self.name}'s trip to the {shop.name} costs {total_cost}"
            )
        suitable_cost = min(comparison_dict)
        if self.money < suitable_cost:
            print(f"{self.name} doesn't have enough "
                  f"money to make purchase in any shop")
        else:
            shop_to_ride = comparison_dict[suitable_cost]
            print(f"{self.name} rides to {shop_to_ride.name}\n")
            return shop_to_ride


class Car:

    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

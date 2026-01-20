from math import dist

from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            location: list,
            money: int,
            product_cart: dict,
            car: dict
    ) -> None:
        self.name = name
        self.location = location
        self.money = money
        self.product_cart = product_cart
        self.car = Car(**car)

    def calculate_cost_of_product_cart(self, shop: Shop) -> int | float:
        total_cost = 0
        for product in self.product_cart:
            total_cost += shop.products[product] * self.product_cart[product]

        return total_cost

    def calculate_distance(self, shop_location: list) -> float:
        return dist(self.location, shop_location)

    def calculate_fuel_cost(self, distance: float, fuel_price: float) -> float:
        return (distance / 100) * self.car.fuel_consumption * fuel_price

    def calculate_total_trip_cost(
            self,
            shop: Shop,
            fuel_price: float
    ) -> float:
        total_distance = (self.calculate_distance(shop.location) * 2)
        fuel_cost = self.calculate_fuel_cost(total_distance, fuel_price)
        product_cost = self.calculate_cost_of_product_cart(shop)
        return round(fuel_cost + product_cost, 2)

    def make_trip(self, shop: Shop, fuel_price: float) -> None:
        total_cost = self.calculate_total_trip_cost(shop, fuel_price)
        if total_cost <= self.money:
            self.money -= total_cost
            shop.print_receipt(self)
            print(f"{self.name} rides home\n"
                  f"{self.name} now has {self.money} dollars\n")
        else:
            print(f"{self.name} doesn't have enough money "
                  f"to make a purchase in any shop\n")

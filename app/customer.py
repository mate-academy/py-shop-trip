import datetime
from dataclasses import dataclass, field
from math import sqrt
from typing import List, Dict
from app.car import Car
from app.shop import Shop


def format_price(price: float) -> str:
    if float(price).is_integer():
        return str(int(price))
    if round(price, 1) == price:
        return f"{price:.1f}"
    return f"{price:.2f}"


def format_money(amount: float) -> str:
    if float(amount).is_integer():
        return str(int(amount))
    return str(amount)


@dataclass
class Customer:
    name: str
    product_cart: Dict[str, int]
    location: List[int]
    money: float
    car: Car
    home_location: List[int] = field(init=False)

    def __post_init__(self) -> None:
        self.home_location = self.location.copy()

    def distance_to(self, location: List[int]) -> float:
        return sqrt(
            (self.location[0] - location[0]) ** 2
            + (self.location[1] - location[1]) ** 2
        )

    def fuel_cost(self, distance_km: float, fuel_price: float) -> float:
        return (self.car.fuel_consumption * distance_km / 100) * fuel_price

    def trip_cost(self, shop: Shop, fuel_price: float) -> float:
        if not shop.has_all_products(self.product_cart):
            return float("inf")

        dist = self.distance_to(shop.location)
        fuel_total = self.fuel_cost(dist, fuel_price) * 2
        products_cost = shop.cost_of_products(self.product_cart)
        if products_cost is None:
            return float("inf")
        return round(fuel_total + products_cost, 2)

    def can_afford(self, shop: Shop, fuel_price: float) -> bool:
        return self.trip_cost(shop, fuel_price) <= self.money

    def buy_from(self, shop: Shop, fuel_price: float) -> None:
        dist = self.distance_to(shop.location)
        fuel_there = self.fuel_cost(dist, fuel_price)
        fuel_back = fuel_there
        self.location = shop.location.copy()
        products_cost = shop.cost_of_products(self.product_cart)
        total_cost = round(fuel_there + products_cost + fuel_back, 2)

        now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        print(f"\nDate: {now}")
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought:")
        for product, qty in self.product_cart.items():
            price = shop.products.get(product, 0)
            total_price = price * qty
            formatted_price = format_price(total_price)
            print(f"{qty} {product}s for {formatted_price} dollars")

        formatted_total = format_price(products_cost)
        print(f"Total cost is {formatted_total} dollars")
        print("See you again!\n")

        self.location = self.home_location.copy()
        print(f"{self.name} rides home")

        self.money -= total_cost
        self.money = round(self.money, 2)
        formatted_money = format_price(self.money)
        print(f"{self.name} now has {formatted_money} dollars")

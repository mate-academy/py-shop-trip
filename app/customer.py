from .utils import get_distance
from typing import Any, Union
from typing import TYPE_CHECKING
import datetime


class Customer:
    def __init__(
            self,
            name: str,
            location: Union[list, tuple],
            money: Union[int, float],
            product_cart: dict,
            car: Any
    ) -> None:
        self.name = name
        self.location = list(location)
        self.money = money
        self.product_cart = product_cart
        self.car = car
        self.initial_location = list(location)

    def ride_to(self, shop: "Shop") -> None:
        print(f"{self.name} rides to {shop.name}")
        self.location = shop.location.copy()

    def go_home(self) -> None:
        print(f"{self.name} rides home")
        self.location = self.initial_location.copy()

    if TYPE_CHECKING:
        from app.shop import Shop

    def calculate_trip_cost(
            self,
            shop: "Shop",
            fuel_price: float
    ) -> tuple[float, float, float] | None:

        for prod in self.product_cart:
            if prod not in shop.products:
                return None

        products_cost = 0
        for prod, qty in self.product_cart.items():
            products_cost += shop.products[prod] * qty
        distance = get_distance(self.initial_location, shop.location)
        fuel_to = self.car.fuel_needed(distance)
        fuel_back = self.car.fuel_needed(distance)
        total_fuel = fuel_to + fuel_back
        fuel_cost = total_fuel * fuel_price
        total_cost = round(products_cost + fuel_cost, 2)
        fuel_cost = round(fuel_cost, 2)

        return products_cost, fuel_cost, total_cost

    def print_receipt(self, shop: "Shop", products_cost: float) -> None:
        now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print()
        print(f"Date: {now}")
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought:")
        for prod, qty in self.product_cart.items():
            price = shop.products[prod] * qty
            if float(price).is_integer():
                price_str = str(int(price))
            else:
                price_str = f"{price:g}"
            suffix = "s" if qty > 1 else ""
            print(f"{qty} {prod}{suffix} for {price_str} dollars")
        print(f"Total cost is {products_cost:g} dollars")
        print("See you again!")
        print()

    def perform_trip(
            self,
            shop: "Shop",  # <-- замість str
            products_cost: float,
            fuel_cost: float
    ) -> None:
        total_cost = products_cost + fuel_cost
        self.ride_to(shop)
        self.print_receipt(shop, products_cost)
        self.money -= total_cost
        self.go_home()
        self.money = round(self.money, 2)
        print(f"{self.name} now has {self.money:g} dollars")
        print()

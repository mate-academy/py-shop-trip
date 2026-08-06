from dataclasses import dataclass, field
from typing import Any

from app.car import Car
from app.coordinates import Coordinates
from app.shop import Shop


@dataclass
class Customer:
    name: str
    location: Coordinates
    money: int
    car: Car
    product_cart: dict[str, int] = None
    cheapest_shop: Shop | None = field(init=False)
    trip_cost: float = field(init=False)
    receipt: dict = field(init=False)

    def __post_init__(self) -> None:
        if self.product_cart is None:
            self.product_cart = dict()
        self.home_location = self.location
        self.cheapest_shop = None
        self.trip_cost = 0.0
        self.receipt = dict()

    @property
    def total_cost(self) -> float:
        return self.trip_cost + sum(self.receipt.values())

    @staticmethod
    def from_dict(customer: dict[str, Any]) -> "Customer":
        return Customer(
            name=customer.get("name"),
            location=Coordinates(*customer.get("location")),
            product_cart=customer.get("product_cart"),
            money=customer.get("money"),
            car=Car(**customer.get("car"))
        )

    def shopping_cost(self, shop: Shop) -> float:
        trip_cost = round(
            2 * self.car.fuel_cost(self.location.distance(shop.location)), 2
        )
        receipt = shop.groceries_cost(self.product_cart)
        total_cost = sum(receipt.values()) + trip_cost
        if self.cheapest_shop is None or (total_cost < self.total_cost):
            self.cheapest_shop = shop
            self.trip_cost = trip_cost
            self.receipt = receipt
        return total_cost

    def go_shopping(self) -> None:
        if self.total_cost > self.money:
            print(
                f"{self.name} doesn't have enough "
                f"money to make a purchase in any shop"
            )
            return
        print(f"{self.name} rides to {self.cheapest_shop.name}")
        self.location = self.cheapest_shop.location
        self.money -= self.total_cost
        self.cheapest_shop.print_receipt(
            self.name,
            self.product_cart,
            self.receipt,
            sum(self.receipt.values())
        )
        print(f"{self.name} rides home")
        self.location = self.home_location
        print(f"{self.name} now has {self.money} dollars\n")

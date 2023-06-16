from dataclasses import dataclass, asdict
from typing import List

from app.units.location import Location
from app.units.shop import Shop
from app.units.product_cart import ProductCart
from app.units.car import Car


@dataclass
class Customer:
    name: str
    product_cart: ProductCart
    location: Location
    money: float
    car: Car
    shop: Shop | None = None
    trip_cost: float | None = None

    def print_info(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def calculate_all_shops_trip(
            self,
            shops: List[Shop],
            fuel_price: float
    ) -> None:
        for shop in shops:
            trip_cost = self.calculate_shop_trip(shop, fuel_price)
            if (
                (self.shop is None or self.trip_cost > trip_cost)
                and self.money >= trip_cost
            ):
                self.shop = shop
                self.trip_cost = trip_cost

    def calculate_shop_trip(self, shop: Shop, fuel_price: float) -> float:
        road_cost = self.calculate_road_cost(shop, fuel_price)
        total_amount = sum(
            [
                shop.calculate_purchases(article=article, quantity=quantity)
                for article, quantity in asdict(self.product_cart).items()
            ]
        )
        trip_cost = sum([road_cost * 2, total_amount])
        print(
            f"{self.name}\'s trip to the {shop.name} "
            f"costs {trip_cost:.2f}"
        )
        return trip_cost

    def calculate_road_cost(self, shop: Shop, fuel_price: float) -> float:
        return (
            (self.location - shop.location)
            * fuel_price * self.car.fuel_consumption / 100
        )

    def shop_trip(self) -> None:
        if self.shop is None:
            print(
                f"{self.name} doesn't have enough "
                "money to make a purchase in any shop"
            )
        else:
            print(f"{self.name} rides to {self.shop.name}\n")
            self.shop.purchase(self.name, self.product_cart)
            self.money -= self.trip_cost
            print(
                f"{self.name} rides home\n"
                f"{self.name} now has {self.money:.2f} dollars\n"
            )

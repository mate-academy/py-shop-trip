from math import dist

from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
        self,
        name: str,
        product_cart: dict,
        location: list,
        money: int,
        car: dict,
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(**car)

    def calculating_trip_cost(self, shop: Shop) -> float:
        distance = dist(self.location, shop.location)
        fuel_amount = self.car.fuel_consumption * distance / 100
        fuel_cost = (fuel_amount * self.car.fuel_price) * 2

        products_cost = 0
        for product, value in self.product_cart.items():
            products_cost += shop.products.get(product, 0) * value

        return round(fuel_cost + products_cost, 2)

    def best_shop_choosing(self, shops: list[Shop]) -> Shop | None:
        print(f"{self.name} has {self.money} dollars")
        for shop in shops:
            print(
                f"{self.name}'s trip to the {shop.name} "
                f"costs {self.calculating_trip_cost(shop)}"
            )

        best_choice = min(
            shops, key=lambda shop_: self.calculating_trip_cost(shop_)
        )
        if self.calculating_trip_cost(best_choice) <= self.money:
            print(f"{self.name} rides to {best_choice.name}\n")
            return best_choice
        print(
            f"{self.name} doesn't have enough money "
            f"to make a purchase in any shop"
        )
        return None

    def shopping_done(self, shop: Shop) -> None:
        print(f"{self.name} rides home")
        money_left = self.money - self.calculating_trip_cost(shop)
        print(f"{self.name} now has {money_left} dollars\n")

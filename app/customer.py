from typing import Dict
from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
        self,
        name: str,
        money: float,
        product_cart: Dict[str, int],
        location: list,
        car: Car,
    ) -> None:
        self.name = name
        self.money = money
        self.product_cart = product_cart
        self.location = location
        self.car = car

    def trip_cost(self, shop: Shop, fuel_price: float) -> float:
        distance = (
            (self.location[0] - shop.location[0]) ** 2
            + (self.location[1] - shop.location[1]) ** 2
        ) ** 0.5
        fuel_cost = distance * 2 * self.car.fuel_consumption / 100 * fuel_price
        products_cost = sum(
            self.product_cart[p] * shop.products[p]
            for p in self.product_cart
            if p in shop.products
        )
        return fuel_cost + products_cost

    def go_shopping(self, shop: Shop, fuel_price: float) -> None:
        total_cost = self.trip_cost(shop, fuel_price)
        if self.money >= total_cost:
            print(f"{self.name} rides to {shop.name}")
            for product, count in self.product_cart.items():
                if product in shop.products:
                    price = count * shop.products[product]
                    print(f"{count} {product}s: ${price:.2f}")
                    self.money -= price
            fuel_cost = total_cost - sum(
                self.product_cart[p] * shop.products[p]
                for p in self.product_cart
                if p in shop.products
            )
            self.money -= fuel_cost
            print(f"{self.name} rides home")

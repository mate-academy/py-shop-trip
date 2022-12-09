from app.car import Car
from app.shop import Shop
from math import sqrt


class Customer:
    def __init__(
        self,
        name: str,
        product_cart: dict,
        location: list[int, int],
        money: int,
        car: Car,
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def print_money(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def print_costs_trip(self, shop: Shop, fuel_price: float) -> None:
        print(
            f"{self.name} trip to the {shop} costs {self.calc_price(shop, fuel_price)} dollars"
        )

    def calc_price(self, shop: Shop, fuel_price: float) -> float:
        products_price = 0
        for product in self.product_cart:
            products_price += (
                self.product_cart[product] * shop.products[product]
            )
        distance_to_shop = sqrt(
            (shop.location[0] - self.location[0]) ** 2
            + (shop.location[1] - self.location[1]) ** 2
        )

        return round(products_price + distance_to_shop * fuel_price, 2)

    def get_cheaper_shop(self, shops: list[Shop], fuel_price) -> Shop:
        cheaper_shop = shops[0]
        for shop in shops:
            if self.calc_price(shop, fuel_price) < self.calc_price(cheaper_shop, fuel_price):
                cheaper_shop = shop
        return cheaper_shop

    def ride_to_shop(self, shop) -> None:
        print(f"Bob rides to {shop}")
        shop.serve_customer(self)

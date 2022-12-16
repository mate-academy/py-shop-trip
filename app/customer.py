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
            f"{self.name}'s trip to the {shop} "
            f"costs {self.calc_trip_price(shop, fuel_price)}"
        )

    def calc_trip_price(self, shop: Shop, fuel_price: float) -> float:
        products_price = sum(
            self.product_cart[product] * shop.products[product]
            for product in self.product_cart
        )

        path_price = self.calc_path_to_shop_price(shop, fuel_price)
        return round(products_price + path_price, 2)

    def calc_path_to_shop_price(self, shop: Shop, fuel_price: float) -> float:
        distance_to_shop = sqrt(
            (shop.location[0] - self.location[0]) ** 2
            + (shop.location[1] - self.location[1]) ** 2
        )
        price_to_one_way = (
            (distance_to_shop * self.car.fuel_consumption) / 100
        ) * fuel_price
        return round(price_to_one_way * 2, 2)

    def get_cheaper_shop(self, shops: list[Shop], fuel_price: float) -> Shop:
        cheaper_shop = shops[0]
        for shop in shops:
            if self.calc_trip_price(shop, fuel_price) < self.calc_trip_price(
                cheaper_shop, fuel_price
            ):
                cheaper_shop = shop
        return cheaper_shop

    def ride_to_shop(self, shop: Shop, fuel_price: float) -> None:
        print(f"{self.name} rides to {shop}\n")
        shop.serve_customer(self)
        self.money -= self.calc_path_to_shop_price(shop, fuel_price)
        print(f"{self.name} rides home")
        print(f"{self.name} now has {self.money} dollars\n")

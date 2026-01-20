from __future__ import annotations

from app.car import Car
from app.shop import Shop


class Customer:
    customers = {}

    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list[int],
            money: int | float,
            car: Car
    ) -> None:
        self.__name = name
        self.__product_cart = product_cart
        self.__home_location = location
        self.__current_location = self.__home_location
        self.__money = money
        self.__car = car
        Customer.customers[self.__name] = self

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError("Name should be string")
        self.__name = name

    @property
    def location(self) -> list[int]:
        return self.__current_location

    @location.setter
    def location(self, new_location: list[int]) -> None:
        if not isinstance(new_location, list):
            raise TypeError("Location should be a list")
        for coordinate in new_location:
            if not isinstance(coordinate, int):
                raise TypeError("Coordinates should be integer")
        self.__current_location = new_location

    @property
    def product_cart(self) -> dict:
        return self.__product_cart

    @product_cart.setter
    def product_cart(self, product_cart: dict) -> None:
        if not isinstance(product_cart, dict):
            raise TypeError("Product cart should be dictionary")
        for product, amount in product_cart.items():
            if not isinstance(product, str):
                raise TypeError("Product name should be a string value")
            elif not isinstance(amount, (int, float)):
                raise TypeError("Product amount should be numeric")
            elif amount < 0:
                raise ValueError("Product amount can't be negative")
        self.__product_cart = product_cart

    @property
    def car(self) -> Car:
        return self.__car

    @car.setter
    def car(self, car: Car) -> None:
        if not isinstance(car, Car):
            raise TypeError("Car attribute should be Car instance")
        self.__car = car

    @property
    def money(self) -> int | float:
        return self.__money

    @money.setter
    def money(self, new_amount_money: int | float) -> None:
        if not isinstance(new_amount_money, (int, float)):
            raise TypeError("Money attribute should be numeric")
        if new_amount_money < 0:
            raise ValueError("Money attribute can't be negative")
        self.__money = new_amount_money

    def shop_trip_cost(self, shop: Shop) -> float:
        distance_to_shop = ((self.location[0] - shop.location[0]) ** 2
                            + (self.location[1] - shop.location[1])
                            ** 2) ** 0.5
        products_cost = sum([
            price * self.product_cart.get(product)
            for product, price in shop.products_price.items()
        ])
        return round(
            products_cost
            + distance_to_shop * 2
            * self.car.fuel_price_per_1_km, 2
        )

    def is_able_to_shop(self, shop: Shop) -> bool:
        return self.money >= self.shop_trip_cost(shop)

    def get_optimal_shop(self, shops: list[Shop]) -> Shop:
        optimal_shop = shops[0]
        for shop in shops[1:]:
            if self.shop_trip_cost(shop) < self.shop_trip_cost(optimal_shop):
                optimal_shop = shop
        return optimal_shop if self.is_able_to_shop(optimal_shop) else None

    def go_shopping(self, shop: Shop) -> None:
        print(f"{self.name} rides to {shop.name}")
        self.location = shop.location
        shop.print_receipt(self)
        print(f"{self.name} rides home")
        self.location = self.__home_location
        self.money -= self.shop_trip_cost(shop)
        print(f"{self.name} now has {self.money} dollars\n")

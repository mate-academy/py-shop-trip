import math

from app.shop import Shop
from app.car import Car


class Person:
    def __init__(
            self,
            name: str,
            product_cart: dict[str: int],
            coordinates: list[int],
            money: float,
            car: Car
    ) -> None:

        self.name = name
        self.product_cart = product_cart
        self.coordinates = self.home_coordinates = coordinates
        self.money = money
        self.car = car

    def calculate_trip_price(self, shop: Shop, fuel_price: float) -> float:

        total_distance = (math.dist(self.coordinates, shop.coordinates) * 2)
        fuel_need = self.car.fuel_need(total_distance)
        total_products_cost = shop.calculate_cart_cost(self.product_cart)
        total_price = round(fuel_need * fuel_price + total_products_cost, 2)
        print(f"{self.name}'s trip to the {shop.name} costs {total_price}")
        return total_price

    def choose_the_cheapest_option(
            self,
            shops: list[Shop],
            fuel_price: float
    ) -> (Shop, float):

        _min = self.calculate_trip_price(shops[0], fuel_price)
        min_index = 0

        for shop_number in range(1, len(shops)):
            price = self.calculate_trip_price(shops[shop_number], fuel_price)
            if price < _min:
                _min = price
                min_index = shop_number

        return shops[min_index], _min

    def check_is_enough_money(self, total_trip_price: float) -> bool:
        if self.money >= total_trip_price:
            return True
        return False

    def market_trip(self, markets: list[Shop], fuel_price: float) -> None:

        print(f"{self.name} has {self.money} dollars")

        cheapest_market, cheapest_cost = (
            self.choose_the_cheapest_option(markets, fuel_price)
        )
        if not self.check_is_enough_money(cheapest_cost):
            print(f"{self.name}"
                  f" doesn't have enough money to make a purchase in any shop")
            return
        print(f"{self.name} rides to {cheapest_market.name}\n")

        self.coordinates = cheapest_market.coordinates

        cheapest_market.purchase_receipt(self.name, self.product_cart)

        print(f"\n{self.name} rides home")
        self.coordinates = self.home_coordinates
        self.money -= cheapest_cost
        print(f"{self.name} now has {self.money} dollars\n")

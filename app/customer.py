from math import sqrt
from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(self,
                 name: str,
                 product_cart: dict,
                 location: list[int],
                 money: float,
                 car: dict) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(car["brand"], car["fuel_consumption"])

    def distance_to(self, shop_location: list[int]) -> float:
        return sqrt(
            (self.location[0] - shop_location[0]) ** 2
            + (self.location[1] - shop_location[1]) ** 2
        )

    def calculate_total_trip_cost(self,
                                  shop: Shop,
                                  fuel_price: float) -> float:
        distance = self.distance_to(shop.location)
        fuel_cost_to_road = (self.car.calculate_fuel_cost(distance, fuel_price)
                             * 2)
        product_cost = shop.calculate_product_cost(self.product_cart)
        return fuel_cost_to_road + product_cost

    def buy_products(self, shop: Shop, fuel_price: float) -> None:
        total_trip_cost = self.calculate_total_trip_cost(shop, fuel_price)
        if self.money >= total_trip_cost:
            print(f"{self.name} rides to {shop.name}")
            self.location = shop.location
            shop.print_receipt(self.name, self.product_cart)
            self.money -= total_trip_cost
            print(f"{self.name} rides home")
            self.location = [0, 0]
            print(f"{self.name} now has {round(self.money, 2)} dollars\n")
        else:
            print(f"{self.name} doesn't have enough money "
                  f"to make a purchase in any shop")

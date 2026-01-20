import datetime
from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(self, name: str,
                 product_cart: dict,
                 location: list,
                 money: int | float,
                 car: Car) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def calculate_trip_cost(self, shop: Shop) -> float:
        distance_to_shop = self.calculate_distance(shop.location)
        fuel_cost_to_shop = self.car.calculate_fuel_cost(distance_to_shop)
        product_cost = self.calculate_product_cost(shop)
        fuel_cost_home = self.car.calculate_fuel_cost(distance_to_shop)
        return fuel_cost_to_shop + product_cost + fuel_cost_home

    def calculate_distance(self, location: list) -> float:
        return ((self.location[0] - location[0]) ** 2
                + (self.location[1] - location[1]) ** 2) ** 0.5

    def calculate_product_cost(self, shop: Shop) -> float:
        cost = 0
        for product, quantity in self.product_cart.items():
            cost += shop.products[product] * quantity
        return cost

    def ride_to_shop(self, shop: Shop) -> None:
        print(f"{self.name} rides to {shop.name}")
        self.location = shop.location

    def buy_products(self, shop: Shop) -> None:
        print(f"\nDate: {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}")
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought:")
        for product, quantity in self.product_cart.items():
            print(f"{quantity} "
                  f"{product}s for "
                  f"{shop.products[product] * quantity} dollars")
        print(f"Total cost is {self.calculate_product_cost(shop)} dollars")
        print("See you again!")
        self.money -= self.calculate_product_cost(shop)

    def ride_home(self) -> None:
        print(f"\n{self.name} rides home")
        self.location = [12, -2]

import math

from app.car import Car


class Customer:
    def __init__(self, customer_info: dict) -> None:
        self.name: str = customer_info["name"]
        self.product_cart: dict = customer_info["product_cart"]
        self.location: list[int] = customer_info["location"]
        self.home_location: list[int] = customer_info["location"]
        self.money: int = customer_info["money"]
        self.car: Car = Car(customer_info["car"])

    def trip_cost(self, shop: object, fuel_price: float) -> float:
        distance = math.dist(self.location, shop.location)
        road_costs = self.car.get_fuel_cost(fuel_price, distance * 2)
        purchase_cost = shop.get_summ_for_products(self.product_cart)
        return road_costs + purchase_cost

    def drive_to_shop(self, shop: object, trip_cost: float) -> None:
        print(f"{self.name} rides to {shop.name}\n")

        self.location = shop.location
        shop.print_recipe(self)

        print(f"{self.name} rides home")

        self.money -= trip_cost
        print(f"{self.name} now has {round(self.money, 2)} dollars\n")
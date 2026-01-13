import math
from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: float,
            car_data: dict) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.home_location = list(location)
        self.money = money
        self.car = Car(car_data["brand"], car_data["fuel_consumption"])

    def calculate_distance(self, target_location: list) -> float:
        return math.sqrt(
            (target_location[0] - self.location[0]) ** 2
            + (target_location[1] - self.location[1]) ** 2
        )

    def calculate_trip_cost(self, shop: Shop, fuel_price: float) -> float:
        distance_to_shop = self.calculate_distance(shop.location)
        fuel_cost_one_way = ((distance_to_shop / 100)
                             * self.car.fuel_consumption * fuel_price)
        products_cost = shop.get_basket_cost(self.product_cart)
        total_cost = (fuel_cost_one_way * 2) + products_cost
        return round(total_cost, 2)

    def perform_trip(self, shop: Shop, total_cost: float) -> None:
        print(f"{self.name} rides to {shop.name}")
        self.location = list(shop.location)
        products_cost = shop.get_basket_cost(self.product_cart)
        shop.print_receipt(self.name, self.product_cart, products_cost)
        print(f"{self.name} rides home")
        self.location = list(self.home_location)
        self.money -= total_cost
        print(f"{self.name} now has {round(self.money, 2)} dollars\n")

import math
from dataclasses import dataclass
from app.car import Car
from app.shop import Shop


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: list
    money: float
    car: Car

    def __post_init__(self) -> None:
        self.car = Car(**self.car)

    def calculate_distance(self, shop: Shop) -> int:
        x1, y1 = self.location
        return int(math.sqrt(
               (shop.location[0] - x1) ** 2 + (shop.location[1] - y1) ** 2))

    def calculate_trip_cost(self, shops: list[Shop],
                            fuel_price: float) -> tuple:
        print(f"{self.name} has {self.money} dollars")
        trip_costs = dict()
        for shop in shops:
            if all(product in shop.products
                   for product in self.product_cart):
                road_cost = round(fuel_price * self.car.fuel_consumption *
                                  self.calculate_distance(shop) / 100, 2)
                trip_costs[shop] = round(road_cost
                                         + shop.calculate_price(self), 2)
                print(f"{self.name}'s trip to the {shop.name}"
                      f" costs {trip_costs[shop]}")
            else:
                raise ValueError
        cheapest = min(trip_costs, key=lambda x: trip_costs[x])
        return cheapest, trip_costs[cheapest],

    def trip_to_cheapest(self, shop: Shop, total_cost: float) -> bool:
        if self.money >= total_cost:
            self.money -= shop.buy_products(self)
            self.location = shop.location
            print(f"{self.name} rides home\n"
                  "=========================================================")
            return True
        return False

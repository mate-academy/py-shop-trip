from app.car import Car

import math


class Customer:
    def __init__(
            self,
            name: str,
            products_to_buy: dict,
            location: list,
            money: int | float,
            car: Car
    ) -> None:
        self.name = name
        self.products_to_buy = products_to_buy
        self.location = location
        self.money = money
        self.car = car

    def get_distance_to(self, target_location: list) -> float:
        distance = math.sqrt(
            (target_location[0] - self.location[0]) ** 2
            + (target_location[1] - self.location[1]) ** 2
        )
        return distance

    def choose_cheapest_shop(self, shops: list, fuel_price: float) -> tuple:
        cheapest_shop = None
        min_cost = float("inf")
        for shop in shops:
            distance = self.get_distance_to(shop.location)
            fuel_cost_one_way = (self.car.fuel_cost_per_km(fuel_price)
                                 * distance)
            products_cost = shop.calculate_product_cost(self.products_to_buy)
            total_cost = fuel_cost_one_way * 2 + products_cost
            print(f"{self.name}'s trip to the {shop.name} "
                  f"costs {round(total_cost, 2)}")
            if total_cost < min_cost:
                min_cost = total_cost
                cheapest_shop = shop
        return cheapest_shop, round(min_cost, 2)

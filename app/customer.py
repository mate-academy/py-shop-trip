from math import sqrt

from app.car import Car


from app.shop import Shop


class Customer:

    def __init__(
        self,
        name: str,
        product_cart: dict[str, int],
        location: list[int],
        money: int,
        car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart.copy()
        self.location = location.copy()
        self.money = money
        self.car = car

    def print_money_info(self, after_purchase: bool = False) -> None:
        if not after_purchase:
            print(f"{self.name} has {self.money} dollars")
        else:
            print(f"{self.name} now has {self.money} dollars\n")

    def get_distance(self, shop: Shop) -> float:
        return sqrt(
            pow(shop.location[0] - self.location[0], 2)
            + pow(shop.location[1] - self.location[1], 2)
        )

    def get_fuel_needed(self, distance: float) -> float:
        return (distance * 2) * (self.car.fuel_consumption / 100)

    @staticmethod
    def get_fuel_cost(fuel_needed: float, fuel_price: float) -> float:
        return fuel_needed * fuel_price

    @staticmethod
    def get_cost_trip(purchase_cost: float, fuel_cost: float) -> float:
        return round(purchase_cost + fuel_cost, 2)

    def print_ride_shop(self, shop_name: str) -> None:
        print(f"{self.name} rides to {shop_name}\n")

    def print_trip_info(self, total_trip_cost: float, shop_name: str) -> None:
        print(
            f"{self.name}'s trip to the {shop_name} costs {total_trip_cost}"
        )

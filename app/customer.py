import datetime

from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list[int],
            money: float,
            car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.home = location
        self.money = money
        self.car = car

    def _calculate_cost_for_trip_to_shop(self, shop: Shop) -> float:
        fuel_cost = (
            ((self._calculate_distance(shop.location)
              * self.car.fuel_consumption) / 100)
            * Car.FUEL_PRICE
        )
        product_cost = 0

        for product_name in self.product_cart:
            product_cost += (
                self.product_cart[product_name]
                * shop.products[product_name]
            )

        total_cost = fuel_cost * 2 + product_cost
        print(f"{self.name}'s trip to the {shop.name} costs {total_cost:.2f}")

        return total_cost

    def choose_min_cost_shop(self, shops: list[Shop]) -> tuple[Shop, float]:
        min_cost = float("inf")
        min_cost_shop = None

        for shop in shops:
            cost_shop = self._calculate_cost_for_trip_to_shop(shop)
            if cost_shop < min_cost:
                min_cost, min_cost_shop = cost_shop, shop

        return min_cost_shop, min_cost

    def has_enough_money(self, cost: float) -> bool:
        return self.money >= cost

    def ride_to_shop(self, shop: Shop) -> None:
        print(f"{self.name} rides to {shop.name}")
        self.money -= (
            ((self._calculate_distance(shop.location)
              * self.car.fuel_consumption) / 100)
            * Car.FUEL_PRICE
        )
        self.location = shop.location

    def buy_products(self, shop: Shop) -> None:
        print(
            f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
            f"Thanks, {self.name}, for your purchase!"
        )
        print("You have bought:")

        total_cost = 0
        for product_name in self.product_cart:
            amount = self.product_cart[product_name]
            cost = shop.products[product_name] * amount
            print(f"{amount} {product_name}s for {cost:g} dollars")
            total_cost += cost

        print(
            f"Total cost is {total_cost} dollars\n"
            f"See you again!"
        )

        self.money -= total_cost

    def ride_back_home(self, shop: Shop) -> None:
        self.location = self.home
        self.money -= (
            ((self._calculate_distance(shop.location)
              * self.car.fuel_consumption) / 100)
            * Car.FUEL_PRICE
        )
        print(f"{self.name} rides home")

    def _calculate_distance(self, other_location: list[int]) -> float:
        return (
            ((self.location[0] - other_location[0]) ** 2
             + (self.location[1] - other_location[1]) ** 2)
            ** 0.5
        )

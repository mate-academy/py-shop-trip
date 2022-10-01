import math

from .transport import Car
from .places import Shop


class Customer:
    def __init__(
        self,
        name: str,
        product_cart: dict[int],
        location: list[int],
        money: int | float,
        car: Car,
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.home = self.location
        self.money = money
        self.car = car

    def shop_trip(self, shops: list[Shop], fuel_cost: int | float) -> None:
        print(f"{self.name} has {self.money} dollars")
        shop, total_cost = self._calculate_prices(shops, fuel_cost)

        if total_cost > self.money:
            return print(
                f"{self.name} doesn't have enough money "
                f"to make purchase in any shop"
            )

        print(f"{self.name} rides to {shop.name}\n")

        # Not sure why it should change if it is not printed, but fine.
        self.location = shop.location

        self._make_purchase(shop, total_cost)

        print(
            f"{self.name} rides home\n"
            f"{self.name} now has {self.money} dollars\n"
        )

        # Set location back to home.
        self.location = self.home

    def _calculate_prices(
        self, shops: list[Shop], fuel_cost: int | float
    ) -> tuple[Shop, float]:
        prices = {}

        for shop in shops:
            round_trip_price = round(
                math.dist(self.location, shop.location)
                * self.car.fuel_consumption
                * fuel_cost
                * 2
                * 0.01,
                2,
            )

            products_price = sum(
                shop.products[product] * amount
                for product, amount in self.product_cart.items()
            )

            prices[shop] = round_trip_price + products_price

            print(
                f"{self.name}'s trip to the {shop.name} "
                f"costs {prices[shop]}"
            )

        cheapest_shop = min(prices, key=prices.get)
        return cheapest_shop, prices[cheapest_shop]

    def _make_purchase(self, shop: Shop, total_cost: float) -> None:
        self.money -= total_cost
        shop.print_receipt(self.name, self.product_cart)

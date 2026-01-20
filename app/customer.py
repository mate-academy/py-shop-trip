from __future__ import annotations
import datetime

from app.car import Car
from app.descriptors import ArgsLoader
from app.location import Location
from app.shop import Shop


class Customer:
    car = ArgsLoader(Car)
    location = ArgsLoader(Location)

    def __init__(
            self,
            name: str,
            product_cart: dict[str, int],
            location: list | Location,
            money: float,
            car: dict | Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def __str__(self) -> str:
        return f"{self.name}, {self.location} ({self.car})"

    def trip(self, shops: list[Shop], fuel_price: float) -> None:
        print(f"{self.name} has {self.money} dollars")

        shops_total_cost = [
            (shop, self._calculate_trip(shop, fuel_price))
            for shop in shops
        ]
        shops_total_cost.sort(key=lambda x: sum(x[1]))
        cheapest_shop, cheapest_trip_cost_tuple = shops_total_cost[0]

        if sum(cheapest_trip_cost_tuple) > self.money:
            print(
                f"{self.name} doesn't have enough "
                f"money to make a purchase in any shop"
            )
            return

        self._trip_shop(cheapest_shop, cheapest_trip_cost_tuple[1])
        self._trip_home(cheapest_trip_cost_tuple[0])

    def _calculate_trip(
            self,
            shop: Shop,
            fuel_price: float
    ) -> tuple[float, float]:
        distance = self.location.get_distance_to(shop.location)
        total_fuel_cost = (
            distance * self.car.fuel_consumption / 100 * fuel_price * 2
        )
        total_products_cost = sum(
            shop.products[product] * amount
            for product, amount in self.product_cart.items()
        )
        total_trip_cost = total_fuel_cost + total_products_cost
        print(
            f"{self.name}'s trip to the {shop.name} "
            f"costs{round(total_trip_cost, 2): g}"
        )
        return total_fuel_cost, total_products_cost

    def _trip_shop(
            self,
            cheapest_shop: Shop,
            total_products_cost: float
    ) -> None:
        print(f"{self.name} rides to {cheapest_shop.name}\n")

        print(f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought:")
        for product, amount in self.product_cart.items():
            cost = cheapest_shop.products[product] * amount
            print(f"{amount} {product}s for{round(cost, 2): g} dollars")
        print(f"Total cost is{round(total_products_cost, 2): g} dollars")
        self.money -= total_products_cost
        print("See you again!\n")

    def _trip_home(self, total_fuel_cost: float) -> None:
        print(f"{self.name} rides home")
        self.money -= total_fuel_cost
        print(f"{self.name} now has{round(self.money, 2): g} dollars\n")

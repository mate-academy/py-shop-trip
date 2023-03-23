import math
import datetime
from dataclasses import dataclass

from app.car import Car
from app.shop import Shop


@dataclass
class Customer:
    name: str
    product_cart: dict[str, int]
    location: list[int]
    money: int
    car: Car

    def select_shop(
            self,
            shops: list[Shop],
            fuel_price: float
    ) -> Shop | None:
        cheapest_trip_cost = 0
        selected_shop: Shop | None = None

        print(f"{self.name} has {self.money} dollars")

        for shop in shops:
            if self.product_cart.keys() <= shop.products.keys():
                fuel_cost = (
                    math.dist(self.location, shop.location)
                    * self.car.fuel_consumption / 100
                    * fuel_price
                )

                products_cost = 0

                for key, value in self.product_cart.items():
                    products_cost += value * shop.products.get(key)

                trip_cost = round(fuel_cost * 2 + products_cost, 2)
                print(f"{self.name}'s trip to the "
                      f"{shop.name} costs {trip_cost}")

                if not cheapest_trip_cost:
                    cheapest_trip_cost = trip_cost
                    selected_shop = shop
                    continue

                if trip_cost < cheapest_trip_cost:
                    cheapest_trip_cost = trip_cost
                    selected_shop = shop

        if cheapest_trip_cost > self.money:
            print(f"{self.name} doesn't have enough money "
                  f"to make a purchase in any shop")

            return

        self.money -= cheapest_trip_cost
        print(f"{self.name} rides to {selected_shop.name}\n")

        return selected_shop

    def make_purchase(self, selected_shop: Shop) -> None:
        date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {date}")
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought: ")

        total_cost = 0

        for key, value in self.product_cart.items():
            cost = selected_shop.products.get(key) * value
            total_cost += cost
            print(f"{value} {key}s for {cost} dollars")

        print(f"Total cost is {total_cost} dollars")
        print("See you again!\n")

    def ride_home(self) -> None:
        print(f"{self.name} rides home")
        print(f"{self.name} now has {round(self.money, 2)} dollars\n")

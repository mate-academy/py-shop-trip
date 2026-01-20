from dataclasses import dataclass
from math import sqrt
from app.car import Car
from app.shop import Shop


@dataclass
class Customer:
    name: str
    location: list
    money: float
    product_cart: dict
    car: Car

    def calculate_distance(self, shop_location: list) -> float:
        return round(
            sqrt(
                (self.location[0] - shop_location[0]) ** 2
                + (self.location[1] - shop_location[1]) ** 2
            ),
            2,
        )

    def try_to_shop(self, shops: list, fuel_price: float) -> None:
        best_shop = None
        best_total_cost = float("inf")

        for shop in shops:
            distance = self.calculate_distance(shop.location)
            fuel_cost = round(
                self.car.calculate_trip_cost(distance * 2, fuel_price), 3
            )
            product_cost = round(
                shop.calculate_total_cost(self.product_cart), 2
            )
            total_trip_cost = round(fuel_cost + product_cost, 2)

            print(
                f"{self.name}'s trip to the {shop.name} "
                f"costs {total_trip_cost}"
            )

            if (
                total_trip_cost < best_total_cost
                and total_trip_cost <= self.money
            ):
                best_total_cost = total_trip_cost
                best_shop = shop

        if best_shop:
            self.go_to_shop(best_shop, best_total_cost, fuel_price)
        else:
            print(
                f"{self.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )

    def go_to_shop(
            self, shop: Shop, total_cost: float, fuel_price: float
    ) -> None:
        print(f"{self.name} rides to {shop.name}")
        shop.print_receipt(self.name, self.product_cart)
        self.money -= total_cost
        self.location = shop.location
        print(f"{self.name} rides home")
        self.location = shop.location
        print(f"{self.name} now has {self.money:.2f} dollars")
        print()

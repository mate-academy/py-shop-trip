import math
import datetime
from dataclasses import dataclass
from typing import Tuple, Dict, Any, List

from app.car import Car
from app.shop import Shop


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: list[int, int]
    money: float
    car: Car

    def calculate_distance(self, shop_location: list[int, int]) -> float:
        return math.sqrt(
            (shop_location[0] - self.location[0]) ** 2
            + (shop_location[1] - self.location[1]) ** 2
        )

    def calculate_trip_cost(
            self,
            distance: float,
            shop: Shop,
            data: Dict[str, Any]
    ) -> float:
        way = self.car.trip_cost(distance * 2, data["FUEL_PRICE"])
        products = shop.calculate_total_cost(self.product_cart)
        return way + products

    @staticmethod
    def choose_cheapest_shop(
            shops: List[Shop],
            all_sum_trip: List[Tuple[float, str]]
    ) -> Shop:
        chosen_shop_name = all_sum_trip[0][1]
        chosen_shop = next(
            shop for shop in shops if shop.name == chosen_shop_name
        )
        return chosen_shop

    def print_way_to_shop(self, chosen_shop: Shop) -> None:
        print(f"{self.name} rides to {chosen_shop.name}\n")

    def print_way_to_home(self) -> None:
        print(f"{self.name} rides home")

    def print_trip_summary(
            self,
            shop: Shop,
            all_sum: Tuple[float, str]
    ) -> None:
        print(f"{self.name}'s trip to the {shop.name} costs {all_sum[0]}")

    def show_receipt(self, chosen_shop: Shop) -> None:
        print("Date:", datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought:")
        total = 0
        for product, amount in self.product_cart.items():
            if product in chosen_shop.products:
                product_name = product if amount == 1 else product + "s"
                if (chosen_shop.products[product] * amount) == int(
                        chosen_shop.products[product] * amount
                ):
                    print(
                        f"{amount} {product_name} for "
                        f"{int(chosen_shop.products[product] * amount)} "
                        f"dollars"
                    )
                else:
                    print(
                        f"{amount} {product_name} for "
                        f"{chosen_shop.products[product] * amount} dollars"
                    )
                total += chosen_shop.products[product] * amount
        print(f"Total cost is {total} dollars")
        print("See you again!\n")

import dataclasses
import math
from typing import Any


@dataclasses.dataclass
class Customer:
    name: str
    location: list
    money: int
    car: dict
    product_cart: dict

    @staticmethod
    def fuel_to_shop(
            fuel_cons: float, distance_to_shop: float, fuel_price: float
    ) -> float:
        return ((fuel_cons * distance_to_shop) / 100 * fuel_price) * 2

    def dist_to_shop(self, shop_location: list) -> float:
        return (
            math.sqrt((shop_location[0] - self.location[0]) ** 2
                      + (shop_location[1] - self.location[1]) ** 2)
        )

    def product_total(self, products: dict) -> int:
        prod_total = 0
        for key_1, value_1 in products.items():
            for key_2, value_2 in self.product_cart.items():
                if key_1 == key_2:
                    prod_total += value_1 * value_2
        return prod_total

    def fuel_expenses(
            self, fuel: float, shop_location: list, fuel_price: float
    ) -> Any:
        fuel_total = round(
            self.fuel_to_shop(
                fuel, self.dist_to_shop(shop_location), fuel_price
            ), 2
        )
        return fuel_total

    def shop_choice(
            self, shop_names: dict, closest_shop: str
    ) -> float:
        total_costs = 0
        for product_name, product_count in self.product_cart.items():
            if product_name in shop_names[closest_shop]:
                product_price = shop_names[closest_shop][product_name]
                product_total_cost = product_price * product_count
                total_costs += product_total_cost
                print(
                    f"{product_count} {product_name}s "
                    f"for {product_total_cost} dollars"
                )
        print(f"Total cost is {total_costs} dollars")
        return total_costs

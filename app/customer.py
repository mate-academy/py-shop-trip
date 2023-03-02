import dataclasses
import math
from typing import Any


@dataclasses.dataclass
class Customer:
    name: str
    location: tuple
    money: int
    car: dict
    product_cart: dict

    @staticmethod
    def fuel_to_shop(
            fuel_cons: float, distance_to_shop: float, fuel_price: float
    ) -> float:
        return ((fuel_cons * distance_to_shop) / 100 * fuel_price) * 2

    def dist_to_shop(self, shop_location: tuple) -> float:
        return (
            math.sqrt((shop_location[0] - self.location[0]) ** 2
                      + (shop_location[1] - self.location[1]) ** 2)
        )

    def product_total(self, products: dict) -> list:
        prod_total = sum(price * count for price, count in zip(
            products.values(),
            self.product_cart.values()
        ))
        return prod_total

    def fuel_expenses(
            self, fuel: float, shop_location: tuple, fuel_price: float
    ) -> Any:
        fuel_total = round(
            self.fuel_to_shop(
                fuel, self.dist_to_shop(shop_location), fuel_price
            ), 2
        )
        return fuel_total

    def shop_choice(self, shop_names: dict, closest_shop: Any) -> float:
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

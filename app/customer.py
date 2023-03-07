import dataclasses
import math

from app.shop import Shop


@dataclasses.dataclass
class Customer:
    name: str
    location: list[int]
    money: int
    car: dict
    product_cart: dict

    @staticmethod
    def fuel_to_shop(
        fuel_cons: float, distance_to_shop: float, fuel_price: float
    ) -> float:
        return ((fuel_cons * distance_to_shop) / 100 * fuel_price) * 2

    def dist_to_shop(self, shop_location: list[int]) -> float:
        return math.sqrt(
            (shop_location[0] - self.location[0]) ** 2
            + (shop_location[1] - self.location[1]) ** 2
        )

    def product_total(self, products: dict) -> float:
        return sum(
            count * products[name] for name, count in self.product_cart.items()
        )

    def fuel_expenses(
        self, fuel: float, shop_location: list[int], fuel_price: float
    ) -> float:
        fuel_total = round(
            self.fuel_to_shop(
                fuel, self.dist_to_shop(shop_location), fuel_price
            ), 2
        )
        return fuel_total

    def shop_choice(self, shop: Shop) -> float:
        total_costs = 0
        for product_name, product_count in self.product_cart.items():
            if product_name in shop.products.keys():
                product_price = shop.products[product_name]
                product_total_cost = product_price * product_count
                total_costs += product_total_cost
                print(
                    f"{product_count} {product_name}s "
                    f"for {product_total_cost} dollars"
                )
        print(f"Total cost is {total_costs} dollars")
        return total_costs

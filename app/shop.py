from __future__ import annotations

import dataclasses


@dataclasses.dataclass
class Shop:
    shop_name: str
    shop_location: list[int]
    shop_prices: dict[str, float]

    @staticmethod
    def create_shop(shops: dict) -> list[Shop]:
        shop_list = [
            Shop(shop["name"], shop["location"], shop["products"])
            for shop in shops
        ]
        return shop_list

    def get_product_cost(
        self, name: str, count: int
    ) -> float:
        return count * self.shop_prices[name]

    def get_product_costs(
        self,
        product_cart: dict[str, int],
    ) -> float:
        return sum(
            self.get_product_cost(name, count)
            for name, count in product_cart.items()
        )

    def sell_products(
        self,
        product_cart: dict[str, int],
    ) -> float:

        print("You have bought: ")

        total_cost = 0
        for product, count in product_cart.items():
            product_cost = self.get_product_cost(product, count)
            total_cost += product_cost

            print(f"{count} {product}s for {product_cost} dollars")

        print(f"Total cost is {total_cost} dollars")

        return total_cost

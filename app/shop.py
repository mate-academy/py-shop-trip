from __future__ import annotations

import dataclasses


@dataclasses.dataclass
class Shop:
    shop_name: str
    shop_location: list[int]
    shop_prices: dict[str, float]

    @staticmethod
    def create_shop(shops: dict) -> list[Shop]:
        shop_list = []
        for shop in shops:
            shop_list.append(
                Shop(
                    shop["name"],
                    shop["location"],
                    shop["products"]
                )
            )
        return shop_list

    def sell_products(
            self,
            product_cart: dict,
            print_indicator: bool = True
    ) -> float:

        if print_indicator:
            print("You have bought: ")

        total_cost = 0
        for product in product_cart:

            product_cost = \
                product_cart[product] * self.shop_prices[product]
            total_cost += product_cost

            if print_indicator:
                print(f"{product_cart[product]} {product}s "
                      f"for {product_cost} dollars")

        if print_indicator:
            print(f"Total cost is {total_cost} dollars")

        return total_cost

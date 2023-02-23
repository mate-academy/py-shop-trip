import dataclasses
from typing import List


@dataclasses.dataclass
class Shop:
    name: str
    location: List[int]
    products: dict

    def total_price(self, product_cart: dict) -> float:
        price = 0
        for product, count in product_cart.items():
            price += self.products[product] * count

        return round(price, 2)

    @classmethod
    def list_read(cls, list_shops: List[dict]) -> list:
        shop_list = []
        for shop in list_shops:
            shop_list.append(Shop(**shop))
        return shop_list

    def buy_product(self, product_cart: dict) -> None:
        total_price = 0

        for product, quantity in product_cart.items():
            price = self.products[product] * quantity
            total_price += price

            print(f"{quantity} {product}s for {price} dollars")

        print(f"Total cost is {total_price} dollars\nSee you again!\n")

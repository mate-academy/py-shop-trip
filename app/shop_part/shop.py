from __future__ import annotations
from dataclasses import dataclass
import datetime

from app.shop_part.product import ShopProduct, ClientCart
from app.customer_part.customer import Customer


@dataclass
class Shop:
    name: str
    location: list[int]
    products: dict["ShopProduct"]

    @classmethod
    def create_shop_from_dict(cls, dict_of_shops: list[dict]) -> dict[Shop]:
        return {
            shop.get("name"): cls(
                name=shop.get("name"),
                location=shop.get("location"),
                products=ShopProduct.create_shop_product_collaction(
                    shop.get("products")
                ),
            )
            for shop in dict_of_shops
        }

    @staticmethod
    def calculate_products_total_price(
        customer_wish_list: dict[ClientCart], shop_products: dict[ShopProduct]
    ) -> float:
        return round(
            sum(
                shop_products[product.name].price * product.count
                for product in customer_wish_list.values()
            ),
            2,
        )

    def take_payment(self, customer: Customer) -> None:
        print(
            f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
            f"Thanks, {customer.name}, for your purchase!\n"
            f"You have bought: "
        )
        for check_item in customer.cart.values():
            print(
                f"{check_item.count} {check_item.name}s for "
                f"{self.products[check_item.name].price * check_item.count} "
                f"dollars"
            )
        print(
            f"Total cost is {customer.option.get('products_price')} dollars\n"
            f"See you again!\n"
        )
        customer.money -= customer.option.get("total_price")

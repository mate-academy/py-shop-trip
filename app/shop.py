from __future__ import annotations


class Shop:
    def __init__(self, name: str, location: list[int], products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    @staticmethod
    def shops_maker(shops_in_dict: dict) -> dict[Shop]:
        shop_instances = {}

        for shop in shops_in_dict:
            shop_instances[shop.get("name")] = Shop(
                name=shop.get("name"),
                location=shop.get("location"),
                products=shop.get("products")

            )

        return shop_instances

    @staticmethod
    def price_vs_wallet_checker(
            min_cost: float,
            money: float,
            name: str
    ) -> bool:

        if min_cost > money:
            print(
                f"{name} "
                f"doesn't have enough money to make purchase in any shop")
            return True

        return False

    @staticmethod
    def make_purchased_products_list(
            customer_products: dict,
            value: dict
    ) -> list[dict]:
        purchased_products = []

        for key in customer_products:
            purchased_products.append(
                {key: {"amount": customer_products[key], "price": value[key]}}
            )

        return purchased_products

    @staticmethod
    def products_total_price_calculator(
            customer_products: dict,
            value: dict
    ) -> int:
        total = 0

        for key in customer_products:
            total += customer_products[key] * value[key]

        return total

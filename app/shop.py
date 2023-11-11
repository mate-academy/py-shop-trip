from math import floor


class Shop:
    def __init__(
            self,
            name: str,
            location: list,
            cost_products: dict
    ) -> None:
        self.name = name
        self.location = location
        self.cost_products = cost_products

    def print_receipt_purchase(
            self,
            name: str,
            product_cart: dict
    ) -> None:
        print()
        print("Date: 04/01/2021 12:33:41")
        print(f"Thanks, {name}, for your purchase!")
        print("You have bought: ")
        total_cost = 0
        for product in product_cart:
            price_product = (
                product_cart[product] * self.cost_products[product]
            )
            if isinstance(price_product, float) and price_product.is_integer():
                price_product = floor(price_product)

            total_cost += price_product
            print(
                f"{product_cart[product]} "
                f"{product}s for {price_product} dollars"
            )
        print(f"Total cost is {total_cost} dollars")
        print("See you again!")

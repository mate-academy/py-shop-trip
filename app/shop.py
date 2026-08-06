from typing import Dict, Union


class Shop:
    def __init__(self, name: str,
                 location: list[int],
                 products: Dict[str, Union[int, float]]) -> None:
        self.name = name
        self.location = location
        self.products = products

    def get_cart_cost(self, product_cart: Dict[str, int]) -> float:
        return float(sum(quantity * self.products[product]
                         for product, quantity in product_cart.items()))

    def print_receipt(self, customer_name: str,
                      product_cart: Dict[str, int],
                      current_date: str) -> None:
        print(f"Date: {current_date}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")

        for product, quantity in product_cart.items():
            product_price = self.products[product]
            cost_per_product = quantity * product_price

            cost_str = int(cost_per_product) \
                if cost_per_product.is_integer() else cost_per_product
            quantity_str = int(quantity) \
                if (isinstance(quantity, float)
                    and quantity.is_integer()) else quantity

            print(f"{quantity_str} {product}s for {cost_str} dollars")

        products_cost = self.get_cart_cost(product_cart)
        prod_cost_str = int(products_cost) \
            if products_cost.is_integer() else products_cost
        print(f"Total cost is {prod_cost_str} dollars")
        print("See you again!\n")

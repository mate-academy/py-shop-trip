import datetime
from typing import Union


class Shop:
    shops = []

    def __init__(self, name: str, location: list[int], products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products
        self.shops.append(self)

    def calc_cost_of_prod_cart(
            self,
            customer: "Customer"
    ) -> Union[int, float]:
        product_cart_cost = 0
        for product, amount in customer.product_cart.items():
            if product in self.products:
                cost_of_product = amount * (self.products[product])
                product_cart_cost += cost_of_product
        return product_cart_cost

    def shop_purchase_reflect(self, customer: "Customer") -> None:
        purchase_datetime = datetime.datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )
        print(f"Date: {purchase_datetime}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought: ")

        for product_name, product_count in customer.product_cart.items():
            product_price = self.products.get(product_name)
            if product_price:
                print(f"{product_count} {product_name}s "
                      f"for {product_price * product_count} dollars")

        total_cost = self.calc_cost_of_prod_cart(customer)
        print(f"Total cost is {total_cost} dollars")
        print("See you again!\n")

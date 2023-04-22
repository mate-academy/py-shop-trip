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
            customer: object
    ) -> Union[int, float]:
        product_cart_cost = 0
        for product, amount in customer.product_cart.items():
            if product in self.products:
                cost_of_product = amount * (self.products[product])
                product_cart_cost += cost_of_product
        return product_cart_cost

    def shop_purchase_reflect(self, customer: object) -> None:
        purchase_datetime = datetime.datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )
        print(f"Date: {purchase_datetime}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought: ")

        milk_count = customer.product_cart.get("milk")
        bread_count = customer.product_cart.get("bread")
        butter_count = customer.product_cart.get("butter")
        print(f"{milk_count} milks for "
              f"{self.products.get('milk') * milk_count} dollars")
        print(f"{bread_count} breads for "
              f"{self.products.get('bread') * bread_count} dollars")
        print(f"{butter_count} butters for "
              f"{self.products.get('butter') * butter_count} dollars")

        total_cost = self.calc_cost_of_prod_cart(customer)
        print(f"Total cost is {total_cost} dollars")
        print("See you again!\n")

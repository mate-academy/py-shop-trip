from typing import Dict
import datetime


class Shop:
    def __init__(self, data: Dict[str, Dict]) -> None:
        self.name = data["name"]
        self.location = data["location"]
        self.products = data["products"]

    def get_product_price(self, product: str, amount: int) -> float:
        if product in self.products:
            return self.products[product] * amount

        print("This product is not available in this store")
        return 0

    def buy_products(
        self,
        customer_name: str,
        product_cart: Dict[str, int]
    ) -> float:
        print(
            datetime.datetime.now().strftime("Date: %d/%m/%Y %H:%M:%S")
        )
        print(f"Thanks, {customer_name}, for you purchase!")
        print("You have bought: ")

        cost_of_bought_products = 0

        for product, amount in product_cart .items():
            cost_of_product = self.get_product_price(product, amount)
            cost_of_bought_products += cost_of_product
            if cost_of_product:
                print(
                    f"{amount} {product}s for "
                    f"{cost_of_product} dollars"
                )

        print(f"Total cost is {cost_of_bought_products} dollars")
        print("See you again!\n")

        return cost_of_bought_products

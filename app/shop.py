import datetime

from typing import Dict


class Shop:
    def __init__(
            self,
            shop_data: Dict[str, Dict]
    ) -> None:
        self.name = shop_data["name"]
        self.products = shop_data["products"]
        self.location = shop_data["location"]

    def calculate_product(
            self,
            product: str,
            amount: int
    ) -> float:
        if product in self.products:
            return self.products[product] * amount

        print("This product is not available in this store")
        return 0

    def buy_products(
            self,
            customer: str,
            required_products: dict
    ) -> int:
        print(datetime.datetime.now().strftime("Date: %d/%m/%Y %H:%M:%S"))
        print(f"Thanks, {customer}, for you purchase!")
        print("You have bought: ")

        price_of_products = 0

        for product, amount in required_products.items():
            price = self.calculate_product(product, amount)
            price_of_products += price
            print(f"{amount} {product}s for {price} dollars")

        print(f"Total cost is {price_of_products} dollars")
        print("See you again!\n")

        return price_of_products

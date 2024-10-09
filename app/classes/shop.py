from dataclasses import dataclass
from datetime import datetime


@dataclass
class Shop:
    name: str
    location: list[int]
    products: dict

    def make_check(self, customer: object) -> str:
        milk_price = self.products.get("milk") * customer.product_cart.get("milk")
        bread_price = self.products.get("bread") * customer.product_cart.get("bread")
        butter_price = self.products.get("butter") * customer.product_cart.get("butter")
        total_price = milk_price + bread_price + butter_price
        return (f"Date: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}\n"
                f"Thanks, {customer.name}, for your purchase!\n"
                f"You have bought:\n"
                f"{customer.product_cart["milk"]} milks for {milk_price} dollars\n"
                f"{customer.product_cart["bread"]} breads for {bread_price} dollars\n"
                f"{customer.product_cart["butter"]} butters for {butter_price} dollars\n"
                f"Total cost is {total_price} dollars\n"
                f"See you again")
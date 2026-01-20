from dataclasses import dataclass
import datetime


@dataclass
class Shop:
    name: str
    location: list[int]
    products: dict

    def make_check(self, customer: object) -> str:
        milk_price = self.products.get(
            "milk") * customer.product_cart.get("milk")
        if milk_price % 1 == 0:
            milk_price = int(milk_price)
        bread_price = self.products.get(
            "bread") * customer.product_cart.get("bread")
        if bread_price % 1 == 0:
            bread_price = int(bread_price)
        butter_price = self.products.get(
            "butter") * customer.product_cart.get("butter")
        if butter_price % 1 == 0:
            butter_price = int(butter_price)
        total_price = milk_price + bread_price + butter_price
        customer.spent_money = total_price
        return (f"Date: "
                f'{datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}\n'
                f"Thanks, {customer.name}, for your purchase!\n"
                f"You have bought" + ":" + "\n"
                f'{customer.product_cart["milk"]} milks for'
                f" {milk_price} dollars\n"
                f'{customer.product_cart["bread"]} breads for '
                f"{bread_price} dollars\n"
                f'{customer.product_cart["butter"]} butters for '
                f"{butter_price} dollars\n"
                f"Total cost is {total_price} dollars\n"
                f"See you again!\n")

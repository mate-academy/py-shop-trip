from datetime import datetime

from app.customer import Customers


class Shops:
    def __init__(self, shop_dict, customer: Customers) -> None:
        self.name = shop_dict["name"]
        self.location = shop_dict["location"]
        self.product = shop_dict["product"]
        self.customer = customer

    def print_receipt(self, customer: Customers) -> None:
        milk_cost = customer.prod_cart["milk"] * self.product["milk"]
        bread = customer.prod_cart["bread"] * self.product["bread"]
        butter = customer.prod_cart["butter"] * self.product["butter"]
        amar = customer.prod_cart["milk"]
        print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        print(f"Thanks, {customer.name}, for you purchase! \n")
        print(f"You have bought:\n"
        f"{customer.location[0]}")
        print(f"{amar} milk for {milk_cost} dollars\n")
              f"{customer.prod_cart["bread"]} ")

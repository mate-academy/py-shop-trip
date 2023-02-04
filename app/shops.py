from datetime import datetime

from app.customer import Customers


class Shops:
    def __init__(self, shop_dict) -> None:
        self.name = shop_dict["name"]
        self.location = shop_dict["location"]
        self.product = shop_dict["product"]

    def get_total(self, customer: Customers) -> float:
        total_cost = sum(
            [customer.prod_cart[key] * self.product[customer.prod_cart[key]]
             for key in customer.prod_cart])
        return round(total_cost, 2)

    def print_receipt(self, customer: Customers) -> None:
        print(
            f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"Thanks, {customer.name}, for you purchase! \n"
            f"You have bought:\n")
        for key in customer.prod_cart:
            print(
                f"{customer.prod_cart[key]} {customer.prod_cart[key].__name__} for "
                f"{customer.prod_cart[key] * self.product[customer.prod_cart[key]]} dollars\n")
        print(f"Total cost is {self.get_total(customer)} dollars\n")
        print("See you again!")


from datetime import datetime
from app.customer import Customer


class Shop:

    def __init__(
            self,
            shop_dict: dict
    ) -> None:
        self.name = shop_dict["name"]
        self.location = shop_dict["location"]
        self.products = shop_dict["products"]

    def shopping(self, customer: Customer) -> None:
        date = datetime(2021, 1, 4, 12, 33, 41)
        print(f"Date: {date.strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {customer.name}, for you purchase!\n"
              f"You have bought: ")
        total_m = customer.product_cart["milk"] * self.products["milk"]
        total_br = customer.product_cart["bread"] * self.products["bread"]
        total_bu = customer.product_cart["butter"] * self.products["butter"]
        print(f"{customer.product_cart['milk']} milks for {total_m}"
              f" dollars\n"
              f"{customer.product_cart['bread']} breads for {total_br}"
              f" dollars\n"
              f"{customer.product_cart['butter']} butters for {total_bu}"
              f" dollars\n"
              f"Total cost is {total_m + total_br + total_bu} dollars\n"
              f"See you again!\n"
              f"\n{customer.name} rides home\n"
              f"{customer.name} now has {customer.money} dollars\n"
              )

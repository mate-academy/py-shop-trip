from datetime import datetime
# from typing import TYPE_CHECKING
# if TYPE_CHECKING:
# from customer import Customers


class Shops:
    list_of_shops = []

    def __init__(self, shop_dict) -> None:
        self.name = shop_dict["name"]
        self.location = shop_dict["location"]
        self.product = shop_dict["products"]
        self.__class__.list_of_shops.append(self)

    def get_total(self, customer) -> float:
        total_cost = sum(
            [customer.prod_cart[key] * self.product[key]
             for key in customer.prod_cart])
        return round(total_cost, 2)

    def print_receipt(self, customer) -> None:
        print(
            f"Date: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
            f"Thanks, {customer.name}, for you purchase! \n"
            f"You have bought:")
        for key in customer.prod_cart:
            print(
                f"{customer.prod_cart[key]} {key} for "
                f"{customer.prod_cart[key] * self.product[key]} dollars")
        print(f"Total cost is {self.get_total(customer)} dollars")
        print("See you again!")


if __name__ == "__main__":
    shops = [{
            "name": "Outskirts Shop",
            "location": [10, -5],
            "products": {
                "milk": 3,
                "bread": 1,
                "butter": 2.5
            }
        },
        {
            "name": "Shop '24/7'",
            "location": [4, 3],
            "products": {
                "milk": 2,
                "bread": 1.5,
                "butter": 3.2
            }
        },
        {
            "name": "Central Shop",
            "location": [0, 0],
            "products": {
                "milk": 3,
                "bread": 2,
                "butter": 3.5
            }
        }]



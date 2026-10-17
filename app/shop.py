import datetime
from app.customer import Customer


class Shop:
    def __init__(
            self, shop_name: str,
            location: tuple,
            products: dict
    ) -> None:
        self.shop_name = shop_name
        self.location = tuple(location)
        self.products = products

    def print_check(self, customer: "Customer") -> None:
        time_of_day = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        total_cost = 0.0
        print()
        print(f"Date: {time_of_day}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        for key, value in customer.product_cart.items():
            cost_of_product = value * self.products[key]
            if cost_of_product == int(cost_of_product):
                cost_of_product = int(cost_of_product)
            total_cost += cost_of_product
            print(f"{value} {key}s for {cost_of_product} dollars")
        print(f"Total cost is {total_cost} dollars")
        print("See you again!")
        print()

from dataclasses import dataclass
import datetime


@dataclass
class Shop:
    name: str
    location: list
    products: dict

    def get_bill(self, customer: list) -> None:
        date_today = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        total_cost = 0

        print(f"Date: {date_today}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")

        for key, value in customer.product_cart.items():
            product_cost = value * self.products[key]

            if product_cost == int(product_cost):
                product_cost = int(product_cost)

            total_cost += product_cost
            print(f"{value} {key}s for {product_cost} dollars")

        print(f"Total cost is {total_cost} dollars\n"
              f"See you again!\n")

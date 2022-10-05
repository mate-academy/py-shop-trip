from dataclasses import dataclass
import datetime


@dataclass
class Shop:
    name: str
    location: list
    products: dict

    def __hash__(self):
        return hash(self.name)

    def form_purchase_receipt(self, customer_name: str, product_cart: dict):
        now = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        print(f"Date: {now}\nThanks, {customer_name}, for you purchase!")
        print("You have bought: ")
        total_product_cost = 0
        for product in product_cart:
            this_product_cost = product_cart[product] * self.products[product]
            print(f"{product_cart[product]} {product}s "
                  f"for {this_product_cost} dollars")
            total_product_cost += this_product_cost
        print(f"Total cost is {total_product_cost} dollars\nSee you again!")

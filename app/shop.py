from dataclasses import dataclass
import datetime


@dataclass
class Shop:
    name: str
    location: list
    products_cost: dict

    def cost_of_products_in_shop(self, product_cart: dict):
        shopping_cost = 0
        for product in product_cart:
            shopping_cost += product_cart[product] * (
                self.products_cost[product]
            )
        return shopping_cost

    def shopping(self, customer):
        print(datetime.datetime.now().strftime("Date: %d/%m/%Y %H:%M:%S"))
        print(f"Thanks, {customer.name}, for you purchase!")
        print("You have bought: ")
        buy_list = customer.product_cart
        total_price = 0
        for product, count in buy_list.items():
            price = self.products_cost[product] * count
            print(f"{count} {product}s for {price} dollars")
            total_price += price
        print(f"Total cost is {total_price} dollars")
        print("See you again!\n")

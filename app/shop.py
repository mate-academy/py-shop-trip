from dataclasses import dataclass
import datetime


@dataclass
class Shop:
    name: str
    location: list
    products: dict

    def calculate_products_cost(self, product_cart: dict) -> float:
        return sum(self.products[product] * quantity
                   for product, quantity in product_cart.items())

    def prints_check(self,
                     customer_name: str,
                     product_cart: dict,
                     product_cost: float) -> None:
        print(f"\n"
              f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %X')}\n"
              f"Thanks, {customer_name}, for your purchase!\n"
              f"You have bought:")
        for product, quantity in product_cart.items():
            cost = self.products[product] * quantity
            if cost == int(cost):
                cost = int(cost)
            print(f"{quantity} {product}s for {cost} dollars")
        print(f"Total cost is {product_cost} dollars\n"
              f"See you again!\n")

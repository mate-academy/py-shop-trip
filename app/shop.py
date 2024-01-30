from dataclasses import dataclass
import datetime


@dataclass
class Shop():
    name: str
    location: list[int, int]
    products: dict

    def purhase(self, customer_name: str, products: dict) -> float:
        current_datetime = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {current_datetime}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")
        total_cost = 0
        for product, qty in products.items():
            sum_product = float(self.products[product]) * qty
            if sum_product.is_integer():
                sum_product = int(sum_product)
            total_cost += sum_product
            print(f"{qty} {product}s for {sum_product} dollars")
        print(f"Total cost is {total_cost} dollars\nSee you again!\n")
        return total_cost

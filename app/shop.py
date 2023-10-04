from dataclasses import dataclass
import datetime


@dataclass
class Shop:
    name: str
    location: list
    products: dict

    def get_price(self, product_cart: dict) -> float:
        total_price = 0
        for product, number in product_cart.items():
            total_price += self.products[product] * number
        return round(total_price, 2)

    def give_receipt(self, customer_name: str, product_cart: dict) -> None:
        total_price = self.get_price(product_cart)
        print(f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought: ")
        for product, number in product_cart.items():
            price = self.products[product] * number
            if price % 1 == 0:
                price = int(price)
            print(f"{number} {product}s for {price} dollars")
        print(f"Total cost is {total_price} dollars")
        print("See you again!")

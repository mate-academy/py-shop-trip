import datetime

from app.customer import Customer


class Shop:
    def __init__(self, name: str, location: list[int], products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_price(self, product_cart: dict) -> float:
        total_price = sum(self.products.get(product, 0) * quantity
                          for product, quantity in product_cart.items())
        return total_price

    def receipt(self, customer: Customer) -> None:
        print(f"Date: {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        for product, quantity in customer.product_cart.items():
            price = self.products.get(product) * quantity
            price = int(price) if price.is_integer() else price
            print(f"{quantity} {product}s for {price} dollars")

        print(f"Total cost is "
              f"{self.calculate_price(customer.product_cart)} dollars")
        print("See you again!\n")

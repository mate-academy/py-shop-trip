import datetime

from app.customer import Customer


class Shop:
    def __init__(self, name: str, location: list[int], products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def get_prices(self, product_cart: dict) -> float:
        total_cost = 0
        for key, value in product_cart.items():
            if price := self.products.get(key):
                total_cost += price * value
        return total_cost

    def print_purchase_receipt(self, customer: Customer) -> None:
        time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {time}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        total_cost = 0
        for key, value in customer.product_cart.items():
            if price := self.products.get(key):
                total_cost += price * value
                formatted_result = "{:.1f}".format(price * value) if \
                    (price * value) % 1 != 0 else str(int(price * value))
                print(f"{value} {key}s for {formatted_result} dollars")
        print(f"Total cost is {total_cost} dollars")
        print("See you again!\n")

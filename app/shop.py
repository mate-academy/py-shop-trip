import datetime


class Shop:
    def __init__(self, name: str, location: list[int], products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_cost(self, product_cart: dict) -> float:
        res = 0
        for key, value in product_cart.items():
            res += value * self.products[key]
        return res

    def print_receipt(self, customer_name: str, product_cart: dict) -> None:
        date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {date}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")

        for product, quantity in product_cart.items():
            cost = quantity * self.products[product]
            print(f"{quantity} {product}s for {round(cost, 2):g} dollars")

        total = self.calculate_cost(product_cart)
        print(f"Total cost is {round(total, 2):g} dollars")
        print("See you again!")

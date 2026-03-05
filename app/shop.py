import datetime


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_products_cost(self, product_cart: dict) -> float:
        cost = 0.0

        for item, quantity in product_cart.items():
            if item in self.products:
                cost += self.products[item] * quantity

        return cost

    def print_receipt(self, customer_name: str, product_cart: dict) -> None:
        now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        print()
        print(f"Date: {now}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")

        total_cost = 0.0

        for item, quantity in product_cart.items():
            if item in product_cart:
                cost = self.products[item] * quantity
                total_cost += cost

                qty_str = int(quantity) if quantity % 1 == 0 else quantity
                cost_str = int(cost) if cost % 1 == 0 else cost

                print(f"{qty_str} {item}s for {cost_str} dollars")

        total_cost_str = int(total_cost) if total_cost % 1 == 0 else total_cost
        print(f"Total cost is {total_cost_str} dollars")
        print("See you again!")
        print()

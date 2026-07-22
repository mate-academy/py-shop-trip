import datetime


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def sell_products(self, products_cart: dict) -> float:
        total_cost = 0
        for product, quantity in products_cart.items():
            if product in self.products:
                total_cost += self.products[product] * quantity
        return total_cost

    def print_receipt(self, customer_name: str,
                      products_cart: dict,
                      total_cost: float) -> None:
        now = datetime.datetime.now()
        print(f"Date: {now.strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")
        for product, quantity in products_cart.items():
            price = self.products[product]
            cost = price * quantity
            if cost.is_integer():
                cost = int(cost)
            print(f"{quantity} {product}s for {cost} dollars")
        print(f"Total cost is {total_cost} dollars")
        print("See you again!")
        print()

import datetime


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def cost_of_products(self, product_cart: dict) -> float:
        total_cost = 0
        for product, quantity in product_cart.items():
            total_cost += self.products[product] * quantity
        return total_cost

    def print_receipt(self, name: str, products: dict) -> None:
        now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"\nDate: {now}")
        print(f"Thanks, {name}, for your purchase!")
        print("You have bought:")
        total = 0
        for product, quantity in products.items():
            cost = self.products[product] * quantity
            total += cost
            f_cost = f"{cost: g}".replace(" ", "")
            print(f"{quantity} {product}s for {f_cost} dollars")

        f_total = f"{total: g}".replace(" ", "")
        print(f"Total cost is {f_total} dollars")
        print("See you again!")

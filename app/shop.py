import datetime


class Shop:
    def __init__(self, name: str, location: tuple, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_product_cost(self, product_cart: dict) -> float | None:
        total_cost = 0
        for product, quantity in product_cart.items():
            if product not in self.products:
                return None
            total_cost += self.products[product] * quantity
        return round(total_cost, 2)

    def print_receipt(self, customer_name: str, product_cart: dict,
                      total_cost: float) -> None:
        now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"\nDate: {now}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")
        for product, quantity in product_cart.items():
            price = self.products[product] * quantity
            print(f"{quantity} {product}s for "
                  f"{f'{price:.2f}'.rstrip('0').rstrip('.')} dollars")
        print(f"Total cost is "
              f"{f'{total_cost:.2f}'.rstrip('0').rstrip('.')} dollars")
        print("See you again!")
        print()

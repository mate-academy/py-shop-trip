import datetime


def format_price(value: float) -> str:
    if value == int(value):
        return str(int(value))  # 12.0 → 12
    elif (value * 10) == int(value * 10):
        return f"{value:.1f}"  # 12.5 → 12.5
    else:
        return f"{value:.2f}"


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def has_products(self, product_cart: dict) -> bool:
        for product in product_cart:
            if product not in self.products:
                return False
        return True

    def product_cost(self, product_cart: dict) -> float:
        product_cost = 0

        for product in product_cart:
            quantity = product_cart[product]
            if not isinstance(quantity, (int, float)) or quantity < 0:
                raise ValueError("Invalid quantity")
            if product not in self.products:
                raise KeyError(f"Product {product} is not in the shop")
            product_cost += quantity * self.products[product]
        return product_cost

    def sell_products(self, product_cart: dict, customer_name: str) -> float:
        total_cost = self.product_cost(product_cart)
        self.print_receipt(customer_name, product_cart, total_cost)
        return total_cost

    def print_receipt(self,
                      customer_name: str,
                      product_cart: dict,
                      total_cost: float,
                      now: str = None) -> None:
        if now is None:
            now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print()
        print(f"Date: {now}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")
        for name, qty in product_cart.items():
            price = self.products[name]
            line_cost = qty * price
            print(f"{qty} {name}{"s" if qty > 1 else ""} "
                  f"for {format_price(line_cost)} dollars")
        print(f"Total cost is {format_price(total_cost)} dollars")
        print("See you again!")
        print()

import datetime


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def get_product_price(self, product_cart: dict) -> float:
        total_price = 0
        for product, quantity in product_cart.items():
            total_price += quantity * self.products[product]
        return round(total_price, 2)

    def print_receipt(self, customer_name: str, product_cart: dict) -> None:
        def fmt(num: int | float) -> int:
            return int(num) if float(num).is_integer() else num

        current_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {current_time}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")

        total_cost = 0
        for product, quantity in product_cart.items():
            price_per_unit = self.products[product]
            item_total = quantity * price_per_unit
            total_cost += item_total

            name = f"{product}s" if quantity > 1 else product

            print(f"{quantity} {name} for {fmt(item_total)} dollars")

        print(f"Total cost is {fmt(total_cost)} dollars")
        print("See you again!")

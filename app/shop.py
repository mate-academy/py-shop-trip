import datetime
from app.customer import Customer


class Shop:

    def __init__(self, name: str,
                 location: list,
                 products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def get_total_price(self, product_cart: dict) -> float:
        total_cost = 0
        for product, count in product_cart.items():
            if product not in self.products:
                return float("inf")
            total_cost += self.products[product] * count
        return round(total_cost, 2)

    def print_receipt(self, customer: Customer) -> None:

        total_cost = self.get_total_price(customer.product_cart)
        if total_cost == float("inf"):
            return  # Просто выходим, чтобы не печатать некорректный чек

        print(f"\nDate: "
              f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")

        for product, count in customer.product_cart.items():
            price = self.products[product]
            item_total = round(price * count, 2)
            display_val = int(item_total) if item_total == int(item_total) \
                else item_total
            print(f"{count} {product}s for {display_val} dollars")

        display_total = int(total_cost) if total_cost == int(total_cost) \
            else total_cost
        print(f"Total cost is {display_total} dollars")
        print("See you again!")

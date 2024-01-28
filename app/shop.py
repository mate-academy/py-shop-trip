import datetime


class Shop:
    def __init__(self, shop_info: dict) -> None:
        self.name = shop_info.get("name")
        self.location = shop_info.get("location")
        self.products = shop_info.get("products")

    def calculate_check(self, product_s: dict, amount: int = None) -> int:
        if amount:
            total = float(amount) * self.products[product_s]
            return int(total) if total.is_integer() else total
        return sum(
            amount * self.products[product]
            for product, amount in product_s.items()
        )

    def purchase_with_receipt(self, visitor: str, products: dict) -> int:
        time_now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {time_now}")
        print(f"Thanks, {visitor}, for your purchase!")
        print("You have bought:")

        expenses = 0
        for product, amount in products.items():
            total = self.calculate_check(product, amount)
            expenses += total
            print(f"{amount} {product}s for {total} dollars")

        print(f"Total cost is {expenses} dollars")
        print("See you again!\n")

        return expenses

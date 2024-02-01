import datetime


class Shop:
    def __init__(self, shop_info: dict) -> None:
        self.name = shop_info.get("name")
        self.location = shop_info.get("location")
        self.products = shop_info.get("products")

    def calculate_one_product(self, product: dict, amount: int) -> int | float:
        total = float(amount) * self.products[product]
        return int(total) if total.is_integer() else total

    def calculate_total_check(self, products: dict) -> int | float:
        return sum(
            amount * self.products[product]
            for product, amount in products.items()
        )

    def purchase(self, visitor: str, products: dict) -> int:
        time_now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {time_now}")
        print(f"Thanks, {visitor}, for your purchase!")
        print("You have bought:")

        for product, amount in products.items():
            total = self.calculate_one_product(product, amount)
            print(f"{amount} {product}s for {total} dollars")

        expenses = self.calculate_total_check(products)
        print(f"Total cost is {expenses} dollars")
        print("See you again!\n")

        return expenses

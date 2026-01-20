import datetime


class Shop:
    def __init__(self, name: str, location: list[int], products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_single_product_cost(
            self,
            product: str,
            amount: int
    ) -> float:
        return self.products.get(product) * amount

    def calculate_product_cost(self, product_cart: dict) -> float:
        total_cost = 0

        for product, amount in product_cart.items():
            total_cost += self.calculate_single_product_cost(product, amount)
        return total_cost

    def print_receipt(self, customer_name: str, product_cart: dict) -> None:
        print(
            f'\nDate: {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}'
        )
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")

        for product, amount in product_cart.items():
            cost = self.calculate_single_product_cost(product, amount)
            formatted_cost = (f"{round(cost, 1)}" if cost % 1 != 0
                              else f"{int(cost)}")
            print(f"{amount} {product}s for {formatted_cost} dollars")

        total_cost = self.calculate_product_cost(product_cart)
        print(f"Total cost is {round(total_cost, 1)} dollars")
        print("See you again!\n")

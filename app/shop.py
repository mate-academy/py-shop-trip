class Shop:
    def __init__(self, name: str, location: list[int], products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_products_cost(self, product_cart: dict) -> float:
        return sum(self.products[product] * quantity for
                   product, quantity in product_cart.items())

    def print_receipt(
            self,
            customer_name: str,
            product_cart: dict,
            products_cost: float
    ) -> None:
        print(f"\nDate: 04/01/2021 12:33:41\n"  # noqa: E231
              f"Thanks, {customer_name}, for your purchase!\n"
              f"You have bought:")  # noqa: E231
        for product, quantity in product_cart.items():
            cost = self.products[product] * quantity
            cost = int(cost) if cost == int(cost) else cost
            print(f"{quantity} {product}s for {cost} dollars")
        print(f"Total cost is {products_cost} dollars\nSee you again!\n")

class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calc_products_cost(self, products_cart: dict) -> float:
        return sum(self.products[product] * quantity
                   for product, quantity in products_cart.items())

    def print_receipt(
            self,
            customer_name: str,
            products_cart: dict,
            products_cost: float
    ) -> None:
        print(f"\n"
              f"Date: 04/01/2021 12:33:41\n"
              f"Thanks, {customer_name}, for your purchase!\n"
              f"You have bought:")
        for product, quantity in products_cart.items():
            cost = self.products[product] * quantity
            if cost == int(cost):
                cost = int(cost)
            print(f"{quantity} {product}s for {cost} dollars")
        print(f"Total cost is {products_cost} dollars\n"
              f"See you again!\n")

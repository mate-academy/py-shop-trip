from datetime import datetime


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def count_total_cost_of_products(self, product_cart: dict) -> float:
        purchase_dict = {
            key: value * self.products[key]
            for key, value in product_cart.items()
            if key in self.products}
        total_cost = 0
        for price in purchase_dict.values():
            total_cost += price
        return total_cost

    def purchase_receipt(self, name: str, product_cart: dict) -> None:
        time_now = datetime.now()
        print(f"Date: {time_now}\n"
              f"Thanks, {name}, for your purchase!\n"
              f"You have bought:\n")
        for key, value in product_cart.items():
            print(f"{value}  {key}s for {purchase_dict[key]} dollars\n")
        print(f"Total cost is {self.count_total_cost_of_products(product_cart)} dollars\n"
              f"See you again!\n")
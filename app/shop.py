import datetime


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def count_total_cost_of_products(self, product_cart: dict) -> float:
        total_cost = 0
        for key, value in product_cart.items():
            if key in self.products:
                price = value * self.products[key]
                total_cost += price
        return total_cost

    def purchase_receipt(self, name: str, product_cart: dict) -> None:
        date_now = datetime.datetime.now()
        receipt_time = date_now.strftime("%d/%m/%Y %H:%M:%S")
        purchase_dict = {
            key: value * self.products[key]
            for key, value in product_cart.items()
            if key in self.products}
        print(f"Date: {receipt_time}\n"
              f"Thanks, {name}, for your purchase!\n"
              f"You have bought:")
        for key, value in product_cart.items():
            print(f"{value} {key}s for {purchase_dict[key]:g} dollars")
        print(f"Total cost is "
              f"{self.count_total_cost_of_products(product_cart)} dollars\n"
              f"See you again!\n")

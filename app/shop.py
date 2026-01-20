import datetime


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_product_cost(self, product_cart: dict) -> list:
        product_cost = []
        for product_name, number in product_cart.items():
            product_cost.append(number * self.products[product_name])
        return product_cost

    def print_bill(self, customer_name: str, product_cart: dict) -> None:
        date_ = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {date_}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")  # noqa E231
        for name, number in product_cart.items():
            cost = number * self.products[name]
            print(f"{number} {name}s for "
                  f"{int(cost) if cost == int(cost) else cost} dollars")
        print(f"Total cost is "
              f"{sum(self.calculate_product_cost(product_cart))} dollars")
        print("See you again!\n")

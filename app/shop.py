from datetime import datetime


class Shop:

    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def purchase(self, customer_name: str, products_list: dict) -> int | float:
        now = datetime(2021, 4, 1, 12, 33, 41)
        now = now.strftime("%m/%d/%Y %H:%M:%S")

        print(f"Date: {now}")

        product_cost = []

        print(f"Thanks, {customer_name}, for your purchase!\n"
              f"You have bought: ")

        for key, value in products_list.items():
            product_cost.append(products_list[key] * self.products[key])

            print(f"{products_list[key]} {key}s for "
                  f"{products_list[key] * self.products[key]} dollars")

        print(f"Total cost is {sum(product_cost)} dollars\n"
              f"See you again!\n")

        return sum(product_cost)

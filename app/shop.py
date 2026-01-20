import datetime


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def total_products_costs(self, product_cart: dict) -> float:
        products_cost = 0
        for product, quantity in product_cart.items():
            if product in self.products:
                products_cost += quantity * self.products[product]
        return round(products_cost, 2)

    def print_receipt(self, name: str, product_cart: dict) -> None:
        time_now = datetime.datetime.now()
        time_now = time_now.strftime("%d/%m/%Y %H:%M:%S")
        receipt = ""
        total_cost = 0
        for key, value in product_cart.items():
            if key in self.products:
                cost = float(value * self.products[key])
                formatted_cost = f"{int(cost)}" if cost.is_integer()\
                    else f"{cost:.1f}"
                result = (f"{value} {key}s for "
                          f"{formatted_cost} dollars\n")
                receipt += result
                total_cost += value * self.products[key]
        receipt += f"Total cost is {total_cost} dollars\n"
        receipt += "See you again!\n"
        print(f"Date: {time_now}\n"
              f"Thanks, {name}, for your purchase!\n"
              "You have bought:")
        print(receipt)

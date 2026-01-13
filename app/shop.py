import datetime


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def get_basket_cost(self, product_cart: dict) -> float:
        total = 0
        for product, quantity in product_cart.items():
            price = self.products.get(product, 0)
            total += price * quantity
        return total

    def print_receipt(
            self,
            customer_name: str,
            product_cart: dict,
            total_cost: float) -> None:
        print("")
        current_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {current_time}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")
        for product, quantity in product_cart.items():
            price = self.products.get(product, 0)
            cost = price * quantity
            cost_display = int(cost) if cost == int(cost) else cost
            print(f"{quantity} {product}s for {cost_display} dollars")
        total_display = int(total_cost) if (total_cost
                                            == int(total_cost)) else total_cost
        print(f"Total cost is {total_display} dollars")
        print("See you again!\n")

import datetime


class Shop:
    def __init__(
        self, name: str, location: list, products: dict
    ) -> None:
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
        self, customer_name: str, product_cart: dict, total_cost: float
    ) -> None:
        print("")
        current_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {current_time}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")

        for product, quantity in product_cart.items():
            price = self.products.get(product, 0)

            raw_cost = price * quantity
            rounded_cost = round(raw_cost, 2)

            cost_display = (
                int(rounded_cost)
                if rounded_cost.is_integer()
                else rounded_cost
            )

            print(f"{quantity} {product}s for {cost_display} dollars")

        rounded_total = round(total_cost, 2)
        total_display = (
            int(rounded_total)
            if rounded_total.is_integer()
            else rounded_total
        )

        print(f"Total cost is {total_display} dollars")
        print("See you again!\n")

from app.utils import get_current_time


class Shop:
    def __init__(
        self, name: str,
            location: tuple[float, float],
            products: dict[str, float]
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def print_receipt(self, customer: any) -> None:
        current_time = get_current_time()
        print(
            f'Date: {current_time.strftime("%d/%m/%Y %H:%M:%S")}\n'
            f"Thanks, {customer.name}, for your purchase!\n"
            f"You have bought:"  # noqa E231
        )
        total_cost = 0
        for product, quantity in customer.product_cart.items():
            cost = self.products[product] * quantity
            total_cost += cost

            if float(cost).is_integer():
                cost_str = f"{int(cost)}"
            else:
                cost_str = f"{cost:.1f}"  # noqa: E231
            print(f"{quantity} {product}s for {cost_str} dollars")

        if float(total_cost).is_integer():
            total_cost_str = f"{int(total_cost)}"
        else:
            total_cost_str = f"{total_cost:.1f}"  # noqa: E231

        print(f"Total cost is {total_cost_str} dollars\n"
              f"See you again!\n")

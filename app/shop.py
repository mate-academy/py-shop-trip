import datetime


class Shop:
    def __init__(
        self, name: str, location: list[int], products: dict[str, float]
    ) -> None:
        self.name: str = name
        self.location: list[int] = location
        self.products: dict[str, float] = products

    def calculate_products_price(self, product_cart: dict[str, int]) -> float:
        """Рахує суму товарів у кошику клієнта за цінами цього магазину."""
        return sum(
            self.products[item] * amount for item, amount in product_cart.items()
        )

    def print_receipt(self, customer_name: str, product_cart: dict[str, int]) -> None:
        current_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {current_time}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")

        total_products_cost = 0.0

        for item, amount in product_cart.items():
            price = self.products[item] * amount
            total_products_cost += price

            display_price = int(price) if price == int(price) else price
            print(f"{amount} {item}s for {display_price} dollars")

        display_total = (
            int(total_products_cost)
            if total_products_cost == int(total_products_cost)
            else total_products_cost
        )
        print(f"Total cost is {display_total} dollars")
        print("See you again!")

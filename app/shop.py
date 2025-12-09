import datetime


class Shop:
    """
    Represents a shop where customers can buy products.
    """

    def __init__(
        self,
        name: str,
        location: list[int],
        products: dict[str, float]
    ) -> None:
        """
        :param name: Shop's name.
        :param location: Shop's [x, y] location.
        :param products: Dictionary of product prices {product_name: price}.
        """
        self.name = name
        self.location = location
        self.products = products

    def get_products_cost(self, product_cart: dict[str, int]) -> float:
        """
        Calculates the total cost of a customer's shopping cart.
        """
        total_cost = 0.0
        for product, quantity in product_cart.items():
            price = self.products.get(product, 0.0)
            total_cost += price * quantity
        return total_cost

    def print_receipt(
        self,
        customer_name: str,
        product_cart: dict[str, int]
    ) -> float:
        """
        Prints a formatted purchase receipt using the current time.
        """
        now = datetime.datetime.now()
        timestamp = now.strftime("%d/%m/%Y %H:%M:%S")

        print(f"\nDate: {timestamp}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")

        total_cost = self.get_products_cost(product_cart)

        for product, quantity in product_cart.items():
            price = self.products.get(product, 0.0)
            cost = price * quantity

            cost_str = f"{cost:.2f}".rstrip("0").rstrip(".")
            print(f"{quantity} {product}s for {cost_str} dollars")

        total_cost_str = f"{total_cost:.1f}".replace(".0", "")
        print(f"Total cost is {total_cost_str} dollars")
        print("See you again!\n")

        return total_cost

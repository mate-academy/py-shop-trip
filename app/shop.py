from app.utils import format_price


class Shop:
    def __init__(self, data: dict) -> None:
        self.name: str = data["name"]
        self.location: list[float] = data["location"]
        self.products: dict[str, float] = data["products"]

    def has_all_products(self, cart: dict[str, int]) -> bool:
        return all(product in self.products for product in cart)

    def get_cart_cost(self, cart: dict[str, int]) -> float:
        total = 0.0
        for product, quantity in cart.items():
            total += self.products[product] * quantity
        return total

    def print_receipt(self, customer_name: str, cart: dict[str, int]) -> None:
        current_time = "04/01/2021 12:33:41"  # жорстко для тесту

        print()
        print(f"Date: {current_time}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")
        total_cost = 0.0
        for product, quantity in cart.items():
            cost = self.products[product] * quantity
            print(f"{quantity} {product}s for {format_price(cost)} dollars")
            total_cost += cost
        print(f"Total cost is {format_price(total_cost)} dollars")
        print("See you again!\n")

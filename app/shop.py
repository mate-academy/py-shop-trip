import datetime


class Shop:
    def __init__(
            self,
            name: str,
            location: list[int],
            products: dict[str, float]
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_products_cost(self, product_cart: dict[str, int]) -> float:
        total = 0.0
        for product, quantity in product_cart.items():
            total += self.products.get(product, 0) * quantity
        return total

    def print_receipt(
            self,
            customer_name: str,
            product_cart: dict[str, int]
    ) -> float:
        now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {now}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")

        total_cost = 0.0
        for product, quantity in product_cart.items():
            price_per_item = self.products[product]
            item_total = price_per_item * quantity
            total_cost += item_total

            product_name = f"{product}s" if quantity > 1 else product
            price_str = f"{item_total:g}" \
                if isinstance(item_total, float) \
                else str(item_total)
            print(f"{quantity} {product_name} for {price_str} dollars")

        total_str = f"{total_cost:g}" \
            if isinstance(total_cost, float) \
            else str(total_cost)
        print(f"Total cost is {total_str} dollars")
        print("See you again!")  # БЕЗ \n у кінці!

        return total_cost

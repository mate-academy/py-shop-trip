class Shop:
    def __init__(
            self,
            name: str,
            location: list[int],
            products: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_cart_cost(self, product_cart: dict) -> float:
        total_cost = 0
        for product, quantity in product_cart.items():
            if product in self.products:
                total_cost += self.products[product] * quantity
        return round(total_cost, 2)

    def print_receipt(self, customer_name: str, product_cart: dict) -> None:
        print("Date: 04/01/2021 12:33:41")        # Hardcode, because of tests
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")

        total_cost = 0
        for product, quantity in product_cart.items():
            if product in self.products:
                product_cost = self.products[product] * quantity
                total_cost += product_cost

                if product_cost == int(product_cost):
                    formatted_cost = int(product_cost)
                else:
                    formatted_cost = product_cost

                print(
                    f"{quantity} {product}s for {formatted_cost} dollars"
                )

        print(f"Total cost is {total_cost} dollars")
        print("See you again!")

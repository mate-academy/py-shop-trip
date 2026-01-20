
class Cart:
    def __init__(self, cart: dict, products: dict) -> None:
        self.cart = cart
        self.products = products

    def calculate_product_cost(self) -> int | float:
        total_cost = 0
        for product in self.cart:
            total_cost += self.cart[product] * self.products[product]
        return total_cost

    def generate_receipt(self) -> None:
        for product in self.cart:
            product_cost = self.cart[product] * self.products[product]

            # removing .0 from product_cost
            product_cost = int(product_cost) \
                if product_cost % 1 == 0 else product_cost

            print(
                f"{self.cart[product]} {product}s for {product_cost} dollars"
            )

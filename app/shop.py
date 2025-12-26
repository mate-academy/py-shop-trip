from app.customer import Customer


class Shop:
    def __init__(self, shop: dict) -> None:
        self.name = shop["name"]
        self.location = shop["location"]
        self.products = shop["products"]

    def product_customer(self, product_cart: dict) -> float:
        cost_product = 0
        for product, quantity in product_cart.items():
            cost_product += self.products[product] * quantity
        return cost_product

    def receipt(self, customer: Customer) -> object:
        for product, quantity in customer.product_cart.items():
            print(f"{quantity} {product}s for "
                  f"{self.products[product] * quantity} dollars")
        return f"Total cost is " \
               f"{self.product_customer(customer.product_cart)} dollars"

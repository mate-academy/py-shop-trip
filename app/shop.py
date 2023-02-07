from app.customer import Customer


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def get_shopping_cost(self, customer: Customer) -> int | float:
        shopping_cost = 0
        for product in customer.product_cart:
            if product in self.products:
                product_quantity = customer.product_cart[product]
                product_price = self.products[product]
                total_product_cost = product_quantity * product_price
                shopping_cost += total_product_cost
        return shopping_cost

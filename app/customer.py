from app.car import Car


class Customer:

    def __init__(self,
                 name: str,
                 product_cart: dict,
                 money: float | int,
                 car: Car,
                 customer_location: list) -> None:
        self.name = name
        self.product_cart = product_cart
        self.money = money
        self.customer_location = customer_location
        self.car = car

    def prod_cost(self, shop_products: dict) -> float:
        total_product_cost = sum(shop_products.get(product, 0) * quantity
                                 for product,
                                 quantity
                                 in self.product_cart.items())
        return total_product_cost

    def has_money(self) -> None:
        print(f"{self.name} has {self.money} dollars")

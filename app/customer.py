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
        total_product_cost = 0

        for product, quantity in self.product_cart.items():
            price = shop_products.get(product, 0)
            cost = price * quantity
            total_product_cost += cost
        return total_product_cost

    def has_money(self) -> None:
        print(f"{self.name} has {self.money} dollars")

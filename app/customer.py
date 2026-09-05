from app.car import Car


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list[int],
            money: int,
            transport: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.transport = transport

    def calculate_product_cost(
            self,
            shop_products: dict
    ) -> int | float:
        cost = 0
        for product, quantity in self.product_cart.items():
            cost += shop_products[product] * quantity
        return cost

    def is_enough_money(self, total_cost: int | float) -> bool:
        return self.money - total_cost >= 0

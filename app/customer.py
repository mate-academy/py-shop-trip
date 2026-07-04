from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(self, data: dict) -> None:
        self.name = data["name"]
        self.product_cart = data["product_cart"]
        self.location = data["location"]
        self.money = data["money"]
        self.car = Car(data["car"])

    def calculate_shopping_costs(self, shop: Shop) -> dict:
        costs = {}
        total_products_cost = 0.0

        for product, quantity in self.product_cart.items():
            product_cost = quantity * shop.products[product]
            costs[product] = product_cost
            total_products_cost += product_cost

        costs["total"] = total_products_cost
        return costs

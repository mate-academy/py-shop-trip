import math


class Shop:
    def __init__(self, shop: dict) -> None:
        self.shop = shop
        self.name = shop["name"]
        self.location = shop["location"]
        self.products = shop["products"]

    def calculate_distance(self, customer_location: list) -> float:
        diff_x = abs(customer_location[0] - self.location[0])
        diff_y = abs(customer_location[1] - self.location[1])
        return math.sqrt(diff_x ** 2 + diff_y ** 2)

    def calculate_products_cost(
            self,
            product_cart: dict
    ) -> tuple[dict, float]:
        item_costs = {}
        total_cost = 0.0

        for product, quantity in product_cart.items():
            cost = self.products[product] * quantity
            formatted_cost = int(cost) if cost == int(cost) else cost
            item_costs[product] = formatted_cost
            total_cost += cost

        formatted_total = int(total_cost) if total_cost == int(total_cost) \
            else total_cost
        return item_costs, formatted_total

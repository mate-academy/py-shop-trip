import math


class Shop:

    def __init__(self, shop: dict):
        self.shop = shop
        self.name = shop["name"]
        self.location = shop["location"]
        self.products = shop["products"]

    def calculate_distance(
            self,
            customer_location: list
    ) -> int | float:
        diff_x = abs(customer_location[0] - self.location[0])
        diff_y = abs(customer_location[1] - self.location[1])
        return math.sqrt(diff_x ** 2 + diff_y ** 2)

    def calculate_products_cost(
            self,
            product_cart: dict
    ) -> list:
        milk_cost = self.products["milk"] * product_cart["milk"]
        bread_cost = self.products["bread"] * product_cart["bread"]
        butter_cost = self.products["butter"] * product_cart["butter"]
        total_cost = (milk_cost + bread_cost + butter_cost)
        return [milk_cost, bread_cost, butter_cost, total_cost]

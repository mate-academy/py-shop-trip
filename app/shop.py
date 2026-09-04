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

    def calculate_products_cost(self, product_cart: dict) -> list:
        milk_cost = self.products["milk"] * product_cart["milk"]
        bread_cost = self.products["bread"] * product_cart["bread"]
        butter_cost = self.products["butter"] * product_cart["butter"]
        total_cost = milk_cost + bread_cost + butter_cost

        milk_c = (
            int(milk_cost)) if milk_cost == int(milk_cost) else milk_cost
        bread_c = (
            int(bread_cost)) if bread_cost == int(bread_cost) else bread_cost
        butter_c = (
            int(butter_cost)) if butter_cost == int(butter_cost) \
            else butter_cost
        total_c = (
            int(total_cost)) if total_cost == int(total_cost) else total_cost

        return [milk_c, bread_c, butter_c, total_c]

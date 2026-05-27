import math


class Customer:
    def __init__(
        self,
        name: str,
        product_cart: list,
        location: list,
        money: int | float,
        car: dict,
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def calculate_cost_to_road(self, shops: list, fuel_price: float) -> dict:
        need_cost_to_shop_trip = {}
        for shop in shops:
            distance = math.dist(self.location, shop.location) * 2
            liters = distance * self.car["fuel_consumption"] / 100
            need_cost_to_shop_trip[shop.name] = round(liters * fuel_price, 2)
        return need_cost_to_shop_trip

    def calculate_products_cost(self, shops: list) -> dict:
        cost_products_in_shop = {}
        for shop in shops:
            product_bill = 0
            for product_name, product_count in self.product_cart.items():
                product_price = shop.products[product_name]
                product_bill += product_count * product_price
            cost_products_in_shop[shop.name] = product_bill
        return cost_products_in_shop

    def get_choice(self, shops: list, fuel_price: float) -> tuple:
        road = self.calculate_cost_to_road(shops, fuel_price)
        bill = self.calculate_products_cost(shops)
        total_cost = {}
        for shop_name, road_price in road.items():
            total_cost[shop_name] = road_price + bill[shop_name]
        chipest_shop = min(total_cost.items(), key=lambda item: item[1])
        chipest_shop_inst = next(
            shop for shop in shops if shop.name == chipest_shop[0]
        )

        return total_cost, chipest_shop[1], chipest_shop_inst

import math

from app.shop import Shop


class Customer:
    def __init__(self, user_info: dict):
        self.name = user_info["name"]
        self.product_cart = user_info["product_cart"]
        self._home_location = user_info["location"]
        self.location = self._home_location
        self.money = user_info["money"]
        self.car = user_info["car"]

    def pay_for_trip(self, amount: float):
        self.money -= amount

    def _products_costs(self, shop: Shop):
        return sum(
            amount * shop.products[product]
            for product, amount in self.product_cart.items()
        )

    def _get_trip_costs(self, shop: Shop, fuel_price: float):
        distance = math.dist(shop.location, self.location)
        fuel_costs = fuel_price * distance * self.car["fuel_consumption"] / 100
        return round(2 * fuel_costs + self._products_costs(shop), 2)

    def get_customer_shop(self, shops: list, fuel_price: float):
        print(f"{self.name} has {self.money} dollars")

        shops_cost = {}
        for shop in shops:
            costs = self._get_trip_costs(shop, fuel_price)
            print(f"{self.name}'s trip to the {shop.name} costs {costs}")
            shops_cost[costs] = shop
        shops_cost = dict(sorted(shops_cost.items()))

        for costs, shop in shops_cost.items():
            if costs <= self.money:
                return shop, costs
        return None, None

    def ride_to_shop(self, shop: Shop):
        self.location = shop.location

    def ride_to_home(self):
        self.location = self._home_location

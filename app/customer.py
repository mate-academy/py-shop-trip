import math


from app.shop import Shop


class Customer:
    def __init__(self, name: str, product_cart: dict,
                 location: list, money: float, car: dict) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def travel_cost(self, shop: Shop, fuel_price: float) -> float:
        distance = math.dist(shop.location, self.location)
        cost = (distance / 100 * self.car["fuel_consumption"]) * 2 * fuel_price
        return round(cost, 2)

    def products_cost(self, shop: Shop) -> float:
        return shop.shopping_cost(self.product_cart)

    def trip_cost(self, shop: Shop, fuel_price: float) -> float:
        travel = self.travel_cost(shop, fuel_price)
        shopping = self.products_cost(shop)
        if shopping is None:
            return None
        return round(travel + shopping, 2)

    def update_money(self, shopping_cost: float, travel_cost: float) -> float:
        self.money = round(self.money - (shopping_cost + travel_cost), 2)
        return self.money

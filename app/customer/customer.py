from app.customer.car import Car
from app.shop import Shop


class Customer:
    def __init__(self, info: dict) -> None:
        self.name = info["name"]
        self.location = info["location"]
        self.home_location = info["location"]
        self.money = info["money"]
        self.product_cart = info["product_cart"]
        self.car = Car(info["car"])

    def calculate_trip_cost(self, fuel_price: float, shop: Shop) -> float:
        customer_x, customer_y = self.location
        shop_x, shop_y = shop.location
        dist = ((customer_x - shop_x) ** 2 + (customer_y - shop_y) ** 2) ** 0.5
        fuel_cost = (dist / 100) * self.car.fuel_consumption * fuel_price * 2

        product_cost = 0
        for name, count in self.product_cart.items():
            if name in shop.products:
                product_cost += shop.products[name] * count

        return round(fuel_cost + product_cost, 2)

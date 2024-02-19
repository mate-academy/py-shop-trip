import math
from app.car import Car
from app.shop import Shop, TripCalculation


class Customer:
    def __init__(self, customer: dict) -> None:
        self.name = customer["name"]
        self.product_cart = customer["product_cart"]
        self.location = customer["location"]
        self.money = customer["money"]
        self.car = Car(customer["car"])

    def trip_fuel_cost(self, shop: Shop) -> float:
        return round((self.car.fuel_consumption / 100)
                     * math.dist(self.location, shop.location)
                     * self.car.FUEL_PRICE * 2, 2)

    def shopping(self, shop: Shop) -> TripCalculation:
        total = 0
        transactions_list = []
        for product_name, amount in self.product_cart.items():
            cost = shop.products[product_name] * amount
            cost = int(cost) if cost == int(cost) else float(cost)
            total += cost
            transactions_list.append(f"{amount} "
                                     f"{product_name}s for {cost} dollars")
        whole_trip_cost = total + self.trip_fuel_cost(shop)
        return TripCalculation(shop, total, whole_trip_cost, transactions_list)

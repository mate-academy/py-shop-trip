import math
from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(self, name: str, location: tuple, money: float,
                 product_cart: dict, car: Car) -> None:
        self.name = name
        self.location = location
        self.money = money
        self.product_cart = product_cart
        self.car = car

    def calculate_trip_cost(self, shop: Shop,
                            fuel_price: float) -> float | None:
        distance = math.dist(self.location, shop.location)
        fuel_cost = self.car.calculate_fuel_cost(distance * 2, fuel_price)
        product_cost = shop.calculate_product_cost(self.product_cart)
        if product_cost is None:
            return None
        return round(fuel_cost + product_cost, 2)

    def choose_best_shop(self, shops: list[Shop],
                         fuel_price: float) -> Shop | None:
        best_shop = None
        best_price = float("inf")
        for shop in shops:
            trip_cost = self.calculate_trip_cost(shop, fuel_price)
            if trip_cost is not None and trip_cost < best_price:
                best_price = trip_cost
                best_shop = shop
        return best_shop if best_shop and best_price <= self.money else None

    def go_shopping(self, shop: Shop, fuel_price: float) -> None:
        trip_cost = self.calculate_trip_cost(shop, fuel_price)
        if trip_cost is None or trip_cost > self.money:
            print(f"{self.name} doesn't have enough "
                  f"money to make a purchase in any shop")
            return
        print(f"{self.name} rides to {shop.name}")
        shop.print_receipt(self.name, self.product_cart,
                           shop.calculate_product_cost(self.product_cart))
        self.money -= trip_cost
        print(f"{self.name} rides home")
        print(f"{self.name} now has {self.money:.2f} dollars\n")

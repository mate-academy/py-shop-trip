import math


class Customer:
    def __init__(
            self, name: str,
            cart: float,
            location: str,
            money: float,
            car: str
    ) -> None:
        self.name = name
        self.cart = cart
        self.location = location
        self.money = money
        self.car = car
        self.home_location = location[:]

    def distance_to(self, shop: str) -> None:
        x1, y1 = self.location
        x2, y2 = shop.location
        return math.dist([x1, y1], [x2, y2])

    def trip_cost(self, shop: str, fuel_price: float) -> float:
        dist = self.distance_to(shop)
        fuel_to = self.car.fuel_cost(dist, fuel_price)
        fuel_back = self.car.fuel_cost(dist, fuel_price)
        products_cost = shop.calculate_cart_cost(self.cart)
        return fuel_to + products_cost + fuel_back

    def can_afford(self, cost: float) -> None:
        return self.money >= cost

    def go_to(self, shop: str) -> str:
        print(f"{self.name} rides to {shop.name}")
        self.location = shop.location[:]

    def go_home(self) -> str:
        print(f"{self.name} rides home")
        self.location = self.home_location[:]

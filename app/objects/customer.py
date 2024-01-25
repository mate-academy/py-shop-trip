from app.objects.shop import Shop
from app.objects.car import Car


class Customer:
    def __init__(self,
                 name: str,
                 product_cart: dict,
                 location: list[int],
                 money: float,
                 car: Car) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car
        self.min_trip_cost = float("inf")
        self.shop_choice = None

    def calculate_distance(self, shop: Shop) -> float:
        return ((self.location[0] - shop.location[0]) ** 2
                + (self.location[1] - shop.location[1]) ** 2) ** .5

    def calculate_fuel_cost(self, distance: float, fuel_price: float) -> float:
        return ((self.car.fuel_consumption / 100)
                * fuel_price * distance)

    def calculate_cart_total(self, shop: Shop) -> float:
        return sum(self.product_cart[product] * shop.products[product]
                   for product in self.product_cart.keys())

    def trip_cost(self, shop: Shop, fuel_price: float) -> float:
        distance = self.calculate_distance(shop)
        fuel_cost = self.calculate_fuel_cost(distance, fuel_price) * 2
        cart_total = self.calculate_cart_total(shop)
        return round(fuel_cost + cart_total, 2)

    def trip_choice(self, shop: Shop, fuel_price: float) -> None:
        trip_cost = self.trip_cost(shop, fuel_price)
        print(f"{self.name}'s trip to the "
              f"{shop.name} costs {trip_cost}")
        if trip_cost < self.min_trip_cost:
            self.min_trip_cost = trip_cost
            self.shop_choice = shop

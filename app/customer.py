from app.car import Car
from app.shop import Shop
from math import sqrt


class Customer:

    def __init__(self,
                 name: str,
                 product_cart: dict,
                 location: list[int],
                 money: int,
                 car: Car) -> None:

        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def money_available(self) -> str:
        print(f"{self.name} has {self.money} dollars")

    def distance_calculation(self, shop: Shop) -> float:
        return sqrt((shop.location[0]
                    - self.location[0])
                    ** 2 + (shop.location[1]
                    - self.location[1]) ** 2)

    def trip_costing(self, shops: dict, fuel_price: float) -> list[tuple]:
        trips = []
        for shop in shops:
            fuel_required = ((self.distance_calculation(shop) / 100)
                             * self.car.fuel_consumption)
            total_cost = 2 * fuel_required * fuel_price + sum(
                self.product_cart[product] * price
                for product, price in shop.products.items())
            print(f"{self.name}'s trip to the "
                  f"{shop.name} costs {round(total_cost, 2)}")
            trips.append((shop, shop.name, total_cost))
        return trips

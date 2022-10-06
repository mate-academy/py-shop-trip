from math import dist

from app.car import Car


class Customer:
    def __init__(self, customers: dict) -> None:
        self.name = customers["name"]
        self.product_cart = customers["product_cart"]
        self.location = customers["location"]
        self.money = customers["money"]
        self.car = customers["car"]
        self.choosen_shop = None
        self.best_price = None

    def calculate_distance_to_shop(self, other: Shop) -> float:
        return dist(self.location, other.location)

    def choose_shop(self, shops: list, fuel_price: float) -> None:
        car = Car(self.car)
        suitable_shops = []

        for shop in shops:
            distance = self.calculate_distance_to_shop(shop)
            product_price = shop.calculate_price(self.product_cart)
            trip_cost = car.road_cost(distance, fuel_price) * 2
            total_cost = round(product_price + trip_cost, 2)
            print(f"{self.name}'s trip to the {shop.name} costs {total_cost}")
            if self.money > total_cost:
                suitable_shops.append((shop, total_cost))
        if suitable_shops:
            choosen_shop, best_price = sorted(suitable_shops,
                                              key=lambda x: x[1])[0]
            print(f"{self.name} rides to {choosen_shop.name}\n")
            self.choosen_shop = choosen_shop
            self.best_price = best_price
        else:
            print(f"{self.name} doesn't have enough money "
                  f"to make purchase in any shop")

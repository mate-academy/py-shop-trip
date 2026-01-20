from typing import Union, Any


class Customer:
    def __init__(
        self,
        name: str,
        product_cart: dict,
        location: list,
        money: int,
        car: Any
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def count_distance_km(self, point: list) -> Union[int, float]:
        x_square = (self.location[0] - point[0]) ** 2
        y_square = (self.location[1] - point[1]) ** 2
        distance = (x_square + y_square) ** 0.5
        return distance

    def count_trip_cost(self, shop: Any, fuel_price: float) -> float:
        distance = self.count_distance_km(shop.location)
        fuel_required = (distance / 100) * self.car.fuel_consumption
        total_cost = 2 * fuel_required * fuel_price + sum(
            self.product_cart[item] * shop.products.get(item, 0)
            for item in self.product_cart
        )
        return round(total_cost, 2)

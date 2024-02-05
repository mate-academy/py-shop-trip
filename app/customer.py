from app.car import Car


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list[int],
            money: float,
            car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def count_money_for_fuel(self,
                             shop_location: list,
                             fuel_price: float) -> float:
        distance = ((shop_location[0] - self.location[0]) ** 2
                    + (shop_location[1] - self.location[1]) ** 2) ** (1 / 2)
        return distance * fuel_price * self.car.fuel_consumption / 100

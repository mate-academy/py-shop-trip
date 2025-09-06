from math import sqrt
from app.customer import Customer
from app.shop import Shop


class Car(Customer):
    def __init__(self, name: str, product_cart: dict, location: list[int], money: int, car: dict) -> None:
        super().__init__(name, product_cart, location, money)
        self.car = car

    def from_to_shop(self, fuel_price: float, shop: Shop) -> None:
        way_to_shop = (sqrt((shop.location[0] - self.location[0]) ** 2 + (shop.location[1] - self.location[1]) ** 2))
        fuel = (way_to_shop / 100) * self.car["fuel_consumption"]
        price_go_to_shop = round(fuel * fuel_price, 2)
        return price_go_to_shop

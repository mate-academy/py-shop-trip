from math import sqrt
from app.parse_all import ParseJsonMixin


class Car(ParseJsonMixin):
    FUEL_PRICE = None

    def __init__(
            self,
            brand: str,
            fuel_consumption: float
    ) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def cost_of_way(
            self,
            customer_location: list[int],
            shop_location: list[int]
    ) -> float:
        x_shop, y_shop = shop_location
        x_customer, y_customer = customer_location
        distance = sqrt((x_customer - x_shop) ** 2
                        + (y_customer - y_shop) ** 2)
        return round(distance / 100
                     * self.fuel_consumption
                     * Car.FUEL_PRICE * 2, 2)

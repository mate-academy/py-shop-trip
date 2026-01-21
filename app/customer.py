from app.car import Car
from decimal import Decimal


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: int | Decimal,
            car: dict
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = [Decimal(str(x)) for x in location]
        self.money = Decimal(str(money))
        self.car = Car(**car)

    def get_fuel_price(
            self,
            shop_location: list,
            fuel_price: float
    ) -> Decimal:
        s_x = shop_location[0]
        s_y = shop_location[1]
        c_x = self.location[0]
        c_y = self.location[1]

        result = (Decimal.sqrt((s_x - c_x) ** 2 + (s_y - c_y) ** 2)
                  .quantize(Decimal("0.001")))
        result = result * 2
        result = ((result / 100 * self.car.fuel_consumption)
                  .quantize(Decimal("0.001")))
        result = ((result * Decimal(str(fuel_price)))
                  .quantize(Decimal("0.01")))

        return result

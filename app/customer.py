from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(self,
                 name: str,
                 produck_cart: dict,
                 location: list,
                 money: int,
                 car: Car) -> None:
        self.name = name
        self.product_cart = produck_cart
        self.location = location
        self.money = money
        self.car = car

    def count_distance_to_shop(self, shop: Shop) -> float:
        distance = (((shop.location[0] - self.location[0]) ** 2)
                    + ((shop.location[1] - self.location[1]) ** 2))
        return distance ** (1 / 2)

    def return_amount_of_fuel_to_shop(self, shop: Shop) -> float:
        distance = self.count_distance_to_shop(shop)
        return self.car.get_fuel_consum_for_km() * distance

    def count_price_of_whole_trip(self,
                                  shop: Shop,
                                  price_of_liter: float) -> float:
        price_of_cart = shop.get_price_for_shoping_cart(self.product_cart)
        return round(price_of_cart + self.return_amount_of_fuel_to_shop(shop)
                     * 2 * price_of_liter, 2)

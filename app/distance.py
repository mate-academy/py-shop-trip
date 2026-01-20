import math


class Distance:
    @staticmethod
    def fuel_price(
        home_location: list,
        shop_location: list,
        volume_of_fuel: float | int,
        price_for_fuel: float,
    ) -> float:
        distance = math.sqrt(
            (shop_location[0] - home_location[0]) ** 2
            + (shop_location[1] - home_location[1]) ** 2
        )
        price = (volume_of_fuel / 100) * distance * price_for_fuel
        return round(price * 2, 2)

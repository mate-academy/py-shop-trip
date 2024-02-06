import dataclasses


@dataclasses.dataclass
class Car:
    brand: str
    fuel_consumption: float

    def fuel_price_calculate(
            self,
            fuel_price: float,
            cust_location: list[int],
            shop_location: list[int]
    ) -> float:
        distance = ((cust_location[0] - shop_location[0]) ** 2
                    + (cust_location[1] - shop_location[1])) ** 0.5
        return (self.fuel_consumption / 100) * distance * fuel_price

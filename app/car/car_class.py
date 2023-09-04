
class Car:
    def __init__(self, car: dict, fuel_price: float) -> None:
        self.brand = car["brand"]
        self.fuel_consumption = car["fuel_consumption"]
        self.fuel_price = fuel_price

    def cost_of_way(
            self,
            customer_location: list[int, int],
            shop_location: list[int, int]
    ) -> float:
        distance = pow(
            pow(shop_location[0] - customer_location[0], 2)
            + pow(shop_location[1] - customer_location[1], 2),
            (1 / 2)
        )
        cost_of_distance = (
            distance * 2 * self.fuel_price * self.fuel_consumption
        ) / 100

        return round(cost_of_distance, 2)

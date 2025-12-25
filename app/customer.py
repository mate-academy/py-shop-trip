class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: int,
            car: dict
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def calculate_trip_cost(
            self,
            shop_location: list,
            fuel_price: float
    ) -> float:
        fuel_consumption = self.car.get("fuel_consumption")
        distance = calculate_distance(self.location, shop_location)

        fuel_cost = (distance / 100) * fuel_consumption * fuel_price
        return fuel_cost


def calculate_distance(location1: list, location2: list) -> float:
    return ((location1[0] - location2[0])
            ** 2 + (location1[1] - location2[1])
            ** 2) ** 0.5

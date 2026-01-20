class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def get_travel_cost(
        self,
        fuel_price: float,
        customer_location: list[int],
        shop_location: list[int],
    ) -> float:
        distance = ((customer_location[0] - shop_location[0]) ** 2
                    + (customer_location[1] - shop_location[1]) ** 2) ** 0.5
        return (self.fuel_consumption / 100) * distance * fuel_price

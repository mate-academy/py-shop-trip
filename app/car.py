class Car:
    def __init__(self, customer_dict: dict) -> None:
        self.customer_dict = customer_dict

    @property
    def fuel_consumption(self) -> float:
        return self.customer_dict["car"]["fuel_consumption"]

    def get_fuel_price(self, distance: float, fuel_price: float) -> float:
        fuel_needed = (distance / 100) * self.fuel_consumption
        cost = fuel_needed * fuel_price

        return cost

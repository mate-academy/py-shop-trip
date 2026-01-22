class Car:
    def __init__(self, brand: str, fuel_cons: float) -> None:
        self.brand = brand
        self.fuel_cons = fuel_cons

    def calc_trip_cost(self,
                       loc1: list[int],
                       loc2: list[int],
                       fuel_price: float) -> float:

        dist = ((loc1[0] - loc2[0]) ** 2 + abs(loc1[1] - loc2[1]) ** 2) ** 0.5
        return 2 * fuel_price * self.fuel_cons * dist / 100

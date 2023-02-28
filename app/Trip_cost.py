class Trip:
    def __init__(self,
                 start_loc: list,
                 end_loc: list,
                 fuel_cost: float,
                 fuel_consumption: float) -> None:
        self.start_loc = start_loc
        self.end_loc = end_loc
        self.fuel_cost = fuel_cost
        self.fuel_consumption = fuel_consumption

    def distance(self) -> float:
        dx = abs(self.start_loc[0] - self.end_loc[0])
        dy = abs(self.start_loc[1] - self.end_loc[1])
        return (dx ** 2 + dy ** 2) ** 0.5

    def cost(self) -> float:
        return self.fuel_cost * self.distance() * self.fuel_consumption / 100

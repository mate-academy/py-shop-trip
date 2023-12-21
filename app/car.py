class Car:
    def __init__(self,
                 owner_name: str,
                 fuel_price: float,
                 brand: str,
                 fuel_consumption: float,
                 home_location: list
                 ) -> None:
        self.owner_name = owner_name
        self.fuel_price = fuel_price
        self.brand = brand
        self.fuel_consumption = fuel_consumption
        self.location = home_location
        self.current_location = home_location

    def distance_two_way_cost(self, target_location) -> float:
        distance = (((self.location[0] - target_location[0])**2
                    + (self.location[1] - target_location[1])**2)) ** 0.5
        cost = round((2*(distance * self.fuel_consumption
                         * self.fuel_price / 100)), 2)
        return cost

    def change_car_location(self, new_location) -> None:
        self.current_location = new_location

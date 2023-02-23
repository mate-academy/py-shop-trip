from app.client_resources.customer import Customer


class Car:
    def __init__(self,
                 brand: str,
                 fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def ride_to_location(self,
                         person: Customer,
                         place: object) -> None:
        person.money -= ((person.location.distance_to(place) / 100)
                         * self.fuel_consumption) * person.fuel_price * 2

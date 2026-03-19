from app.car import Car


class Customer:
    def __init__(self, customer_data: dict) -> None:
        self.name = customer_data["name"]
        self.product_cart = customer_data["product_cart"]
        self.location = customer_data["location"]
        self.money = customer_data["money"]
        self.car = Car(customer_data["car"])

    def find_distance(self, location: list) -> float:
        distance_there_and_back = (
            2 * (
                (self.location[0] - location[0]) ** 2
                + (self.location[1] - location[1]) ** 2
            ) ** 0.5
        )
        return distance_there_and_back

    def find_travel_cost(self, distance: float, fuel_price: float) -> float:
        return distance * fuel_price * self.car.fuel_consumption / 100

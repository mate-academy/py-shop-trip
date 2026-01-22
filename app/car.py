class Car:
    def __init__(
        self,
        fuel_price: float,
        fuel_consumption: float,
        name: str
    ) -> None:

        self.fuel_price = fuel_price
        self.fuel_consumption = fuel_consumption
        self.name = name

    def cost_of_the_trip(
            self, distances: list, cost_of_purchases: list) -> dict:
        cost_of_the_trips = []
        for distance, cost_of_purchase in zip(distances, cost_of_purchases):

            # The cost of a round trip + the cost of purchases
            price = round(distance["distance"] * self.fuel_consumption
                          / 100 * self.fuel_price * 2
                          + cost_of_purchase["total cost"], 2)
            print(f"{self.name}'s trip to the {distance['store name']} "
                  f"costs {price}")
            cost_of_the_trips.append(dict([
                ("store name", distance["store name"]),
                ("individual cost", cost_of_purchase["individual cost"]),
                ("total cost", cost_of_purchase["total cost"]),
                ("cost of the trip", price)
            ]))
        cost_of_the_trips.sort(key=lambda item: item["cost of the trip"])
        return cost_of_the_trips[0]

class Car:
    def __init__(self, fuel_price: float,
                 fuel_consumption: float, brand: str) -> None:
        self.fuel_price = fuel_price
        self.fuel_consumption = fuel_consumption
        self.brand = brand

    def trip_cost(self, distances: list,
                  cost_of_purchases: list) -> dict:
        trip_costs = []
        for distance, cost_of_one_purchase in \
                zip(distances, cost_of_purchases):
            price = round(distance["distance"] * self.fuel_consumption
                          / 100 * self.fuel_price * 2
                          + cost_of_one_purchase["total cost"], 2)
            print(f"{self.brand}'s trip to the {distance['store name']} "
                  f"costs {price}")
            trip_costs.append(dict([
                ("store name", distance["store name"]),
                ("individual cost", cost_of_one_purchase["individual cost"]),
                ("total cost", cost_of_one_purchase["total cost"]),
                ("cost of the trip", price)
            ]))
            trip_costs.sort(key=lambda item: item["cost of the trip"])
            return trip_costs[0]

from app.car import Car


class Customer:
    def __init__(self, customer_data: dict) -> None:
        self.name = customer_data["name"]
        self.product_cart = customer_data["product_cart"]
        self.location = customer_data["location"]
        self.money = customer_data["money"]
        self.car = Car(customer_data["car"])
        self.possible_trips = []

    def print_trips(self) -> None:
        print(f"{self.name} has {self.money} dollars")

        cheapest_trip = min(self.possible_trips,
                            key=lambda trip: trip.trip_cost)

        for trip in self.possible_trips:
            print(f"{self.name}'s {trip}")

        if self.money < cheapest_trip.trip_cost:
            print(f"{self.name} "
                  f"doesn't have enough money to make a purchase in any shop")
        else:
            print(f"{self.name} rides to {cheapest_trip.trip_name}")
            self.location = cheapest_trip.shop.location
            cheapest_trip.shop.print_purchase_receipt(self.product_cart,
                                                      self.name)
            print()
            print(f"{self.name} rides home")
            self.money = self.money - cheapest_trip.trip_cost
            print(f"{self.name} now has {self.money} dollars")
            print()

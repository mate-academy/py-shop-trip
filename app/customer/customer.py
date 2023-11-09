from app.customer.car import Car
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            cart: dict,
            location: list[int, int],
            balance: float,
            car: Car
    ) -> None:
        self.name = name
        self.cart = cart
        self.location = location
        self.balance = balance
        self.car = car

    def calculate_trip_cost_to(self, shop: Shop, fuel_price: float) -> float:
        return round((self.car.calculate_ride_cost_to(self.location,
                                                      shop.location,
                                                      fuel_price) * 2
                      + shop.calculate_total_cost_of(self.name, self.cart)), 2)

    def shop_in(self, shop: Shop, trip_cost: float) -> None:
        home = self.location

        print(f"{self.name} rides to {shop.name}")
        self.location = shop.location
        shop.print_receipt(self.name)
        self.balance -= trip_cost

        print(f"{self.name} rides home")
        self.location = home
        print(f"{self.name} now has {self.balance} dollars\n")

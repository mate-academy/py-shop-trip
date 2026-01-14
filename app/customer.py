from .car import Car


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: float,
            car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def calculate_trips_to_all_shops(
            self,
            shop_list: list,
            fuel_price: float
    ) -> dict:
        trips = {}
        for shop in shop_list:
            shop_cost = shop.receipt_for_products(self.product_cart)
            distance = self.car.calculate_distance(
                self.location,
                shop.location
            )
            fuel_cost_one_way = self.car.calculate_fuel_cost(
                distance,
                self.car.fuel_consumption,
                fuel_price
            )
            total_cost = round(
                shop_cost + fuel_cost_one_way + fuel_cost_one_way, 2
            )
            trips[shop] = total_cost
        return trips

    def calculate_cheapest_trip(self, trips: dict) -> tuple:
        cheapest_shop = min(trips, key=trips.get)
        min_cost = trips[cheapest_shop]
        return cheapest_shop, min_cost

    def update_money(self, amount: float) -> None:
        self.money = round(self.money - amount, 2)

    def go_home(self) -> None:
        print(f"{self.name} rides home")
        print(f"{self.name} now has {self.money} dollars")
        print()

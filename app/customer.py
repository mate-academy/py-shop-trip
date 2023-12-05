from app.car import Car


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list[int],
            money: float, car: Car) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def find_cheapest_shop(self, shops: list, fuel_price: float) -> tuple:

        cheapest_shop = None
        min_trip_cost = float("inf")

        for shop in shops:
            trip_cost = shop.calculate_trip_cost(
                self,
                fuel_price
            )
            print(f"{self.name}\'s trip to the "
                  f"{shop.name} costs {round(trip_cost, 2)}")

            if trip_cost < min_trip_cost and trip_cost <= self.money:
                min_trip_cost = trip_cost
                cheapest_shop = shop

        return cheapest_shop, min_trip_cost

    @staticmethod
    def make_customers(customers_data: dict) -> list:
        return [Customer(
            customers_info["name"],
            customers_info["product_cart"],
            customers_info["location"],
            customers_info["money"],
            Car(
                customers_info["car"]["brand"],
                customers_info["car"]["fuel_consumption"]
            )
        )
            for customers_info in customers_data]

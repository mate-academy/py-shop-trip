from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(self, data: dict) -> None:
        self.name = data["name"]
        self.product_cart = data["product_cart"]
        self.current_location = data["location"]
        self.prev_location = []
        self.money = data["money"]
        self.car = Car(data["car"]["brand"], data["car"]["fuel_consumption"])

    def trip_cost(self, fuel_price: float, shop: Shop) -> float:
        products_price = 0
        for product, count in self.product_cart.items():
            if product in shop.products:
                products_price += count * shop.products[product]
            else:
                return -1
        car_trip_price = self.car.count_trip(
            fuel_price, self.current_location, shop.location
        )
        return round(products_price + 2 * car_trip_price, 2)

    def find_cheapest_shop(
            self, shops: list[Shop], fuel_price: float
    ) -> tuple:
        print(f"{self.name} has {self.money} dollars")
        cheapest_shop = None
        cheapest_trip_price = None
        for shop in shops:
            trip_price = self.trip_cost(fuel_price, shop)

            # Shop don't have all products
            if trip_price == -1:
                continue

            print(f"{self.name}'s trip to the {shop.name} costs {trip_price}")

            if (cheapest_trip_price is None
                    or cheapest_trip_price > trip_price):
                cheapest_trip_price = trip_price
                cheapest_shop = shop

        return cheapest_shop, cheapest_trip_price

    def change_location(self, location: list[int]) -> None:
        self.prev_location = self.current_location
        self.current_location = location

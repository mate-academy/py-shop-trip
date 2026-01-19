from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: int,
            car: dict
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(*car.values())
        print(f"{self.name} has {self.money} dollars")

    def trip_cost(
            self,
            shop: Shop,
            fuel_price: float
    ) -> float:
        products_cost = shop.products_cost(self.product_cart).values()
        fuel_cons = self.car.total_consumption(self.location, shop.location)
        return round(sum(products_cost) + fuel_cons * fuel_price, 2)

    def cheapest_trip(
            self,
            shops: list[Shop],
            fuel_price: float
    ) -> (Shop, float):
        trips_cost = []
        for shop in shops:
            trip_cost = self.trip_cost(shop, fuel_price)
            print(f"{self.name}'s trip to the {shop.name} costs {trip_cost}")
            trips_cost.append(trip_cost)
        cheapest_trip_index = trips_cost.index(min(trips_cost))
        return shops[cheapest_trip_index], trips_cost[cheapest_trip_index]

    def return_home(
            self,
            trip_cost: float,
    ) -> None:
        print(f"{self.name} rides home")
        print(f"{self.name} now has "
              f"{round(self.money - trip_cost, 2)} dollars\n")

from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            products: dict[str, int],
            location: list[int],
            money: float,
            car: Car,
    ) -> None:
        self.name = name
        self.products = products
        self.location = location
        self.home_location = location
        self.money = money
        self.car = car

    def choose_shop(self, shops: list[Shop], fuel_price: float) -> Shop | bool:
        enough_money = False
        shop_trips = {}
        for shop in shops:
            total_cost = (
                self.calculate_trip_cost(shop, fuel_price)
                + self.calculate_product_cost(shop)
            )
            print(
                f"{self.name}'s trip to the {shop.name}"
                f" costs {round(total_cost, 2)}"
            )
            if total_cost < self.money:
                enough_money = True
                shop_trips[shop] = total_cost
        if not enough_money:
            print(
                f"{self.name} doesn't have enough money"
                f" to make a purchase in any shop"
            )
            return False
        cheapest_shop = min(shop_trips, key=shop_trips.get)
        return cheapest_shop

    def buy_products(self, shop: Shop, fuel_price: float) -> None:
        print(f"{self.name} rides to {shop.name}\n")
        self.money -= self.calculate_trip_cost(shop, fuel_price)
        self.location = shop.location
        self.money -= shop.print_receipt(self)

    def return_home(self) -> None:
        self.location = self.home_location
        print(f"{self.name} rides home")
        print(f"{self.name} now has {round(self.money, 2)} dollars\n")

    def calculate_trip_cost(self, shop: Shop, fuel_price: float) -> float:
        fuel_per_km = self.car.fuel_consumption / 100
        trip_cost = (
            self.calculate_distance(shop) * fuel_per_km
            * fuel_price
            * 2
        )
        return trip_cost

    def calculate_product_cost(self, shop: Shop) -> float:
        cost = 0
        for product, price in self.products.items():
            cost += price * shop.products[product]
        return cost

    def calculate_distance(self, shop: Shop) -> float:
        distance = (
            (shop.location[0] - self.location[0]) ** 2
            + (shop.location[1] - self.location[1]) ** 2
        ) ** 0.5
        return distance

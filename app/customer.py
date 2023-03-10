from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list[int],
            money: int,
            car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def calculate_distance(self, shop: Shop) -> float:
        distance = (
            (shop.location[0] - self.location[0])**2
            + (shop.location[1] - self.location[1])**2
        )**0.5
        return distance

    def calculate_fuel_cost(self, shop: Shop, price_for_liter: float) -> float:
        fuel_is_needed = (
            (self.car.fuel_consumption / 100)
            * self.calculate_distance(shop)
        )
        fuel_cost = (fuel_is_needed * price_for_liter * 2)
        return fuel_cost

    def calculate_product_cost(self, shop: Shop) -> float:
        total_cost = 0
        for product, amount in self.product_cart.items():
            product_price = amount * shop.products[product]
            total_cost += product_price
        return total_cost

    def choose_shop(self, price_for_liter: float, shops: list[Shop]) -> Shop:
        print(f"{self.name} has {self.money} dollars")

        shops_trip_costs = {}
        for shop in shops:
            fuel_cost = self.calculate_fuel_cost(shop, price_for_liter)
            product_cost = self.calculate_product_cost(shop)
            trip_cost = round(fuel_cost + product_cost, 2)
            print(
                f"{self.name}'s trip to the {shop.name} costs {trip_cost}"
            )
            if trip_cost < self.money:
                shops_trip_costs[shop] = trip_cost

        if not shops_trip_costs:
            print(f"{self.name} doesn't have enough money to "
                  f"make a purchase in any shop")
        else:
            cheapest_shop = min(shops_trip_costs, key=shops_trip_costs.get)
            print(f"{self.name} rides to {cheapest_shop.name}\n")
            self.location = cheapest_shop.location
            self.money -= shops_trip_costs[cheapest_shop]
            return cheapest_shop

    def return_home(self) -> None:
        print(f"{self.name} rides home")
        print(f"{self.name} now has {self.money} dollars\n")

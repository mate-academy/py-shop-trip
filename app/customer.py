from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list[int],
            money: int,
            car: "Car"
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car
        self.home_location = location

    def find_the_cheapest_trip(self, shops: list["Shop"]) -> tuple:
        total_cost_dict = {}
        customer_trip = ""

        for shop in shops:
            cost_to_get_shop = self.car.calculate_cost_of_trip(
                self.location, shop.location,
            )
            products_cost = shop.calculate_products_cost(self.product_cart)
            total_cost = cost_to_get_shop + products_cost
            total_cost_dict[total_cost] = shop
            customer_trip += (
                f"{self.name}'s trip to the "
                f"{shop.name} costs {total_cost}\n"
            )

        min_total_cost = min(list(total_cost_dict.keys()))
        selected_shop = total_cost_dict[min_total_cost]

        return customer_trip, selected_shop, min_total_cost

    def ride_to_shop(self, shop: "Shop") -> str:
        self.location = shop.location
        trip_cost = self.car.calculate_cost_of_trip(
            self.home_location, shop.location
        )
        self.money = round(self.money - trip_cost, 2)

        return (
            f"{self.name} rides to "
            f"{shop.name}\n\n"
        )

    def ride_home(self) -> str:
        self.location = self.home_location

        return (
            f"{self.name} rides home\n"
            f"{self.name} now has "
            f"{self.money} dollars\n\n"
        )

from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list[int],
            money: float,
            car: dict,
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(**car)

    @staticmethod
    def calculate_distance(
            first_location: list[int], second_location: list[int]
    ) -> float:
        return ((first_location[0] - second_location[0]) ** 2
                + (first_location[1] - second_location[1]) ** 2) ** 0.5

    @staticmethod
    def calculate_fuel_consumption(
            fuel_consumption: float,
            distance: float
    ) -> float:
        return fuel_consumption / 100.0 * distance

    def calculate_trip_cost(
            self,
            shop_location: list[int],
            fuel_price: float
    ) -> float:
        distance = Customer.calculate_distance(self.location, shop_location)
        fuel_consumption = Customer.calculate_fuel_consumption(
            self.car.fuel_consumption, distance
        )
        return fuel_consumption * fuel_price * 2

    def _print_customer_info(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def _find_cheapest_shop(
            self, shops: list[Shop], fuel_price: float
    ) -> tuple[Shop | None, float]:
        cheapest_shop = None
        minimum_total_cost = float("inf")

        for shop in shops:
            trip_cost = self.calculate_trip_cost(shop.location, fuel_price)
            products_cost = shop.calculate_products_cost(self.product_cart)
            total_cost = trip_cost + products_cost

            print(
                f"{self.name}'s trip to the {shop.name} "
                f"costs {round(total_cost, 2)}"
            )

            if total_cost < self.money and total_cost < minimum_total_cost:
                cheapest_shop = shop
                minimum_total_cost = total_cost

        return cheapest_shop, minimum_total_cost

    def _make_purchase(self, shop: Shop, total_cost: float) -> None:
        products_cost = shop.calculate_products_cost(self.product_cart)
        self.money -= total_cost
        print(f"{self.name} rides to {shop.name}")
        shop.print_receipt(self.name, self.product_cart, products_cost)
        print(f"{self.name} rides home")
        print(f"{self.name} now has {round(self.money, 2)} dollars\n")

    def go_shopping(self, fuel_price: float, shops: list[Shop]) -> None:
        self._print_customer_info()
        cheapest_shop, minimum_total_cost = self._find_cheapest_shop(
            shops,
            fuel_price
        )

        if cheapest_shop and self.money >= minimum_total_cost:
            self._make_purchase(cheapest_shop, minimum_total_cost)
        else:
            print(
                f"{self.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )

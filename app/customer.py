from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list[int],
            money: float,
            car: dict
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(**car)

    def calculate_trip_cost(
            self,
            shop_location: list[int],
            fuel_price: float
    ) -> float:
        distance = (
            ((shop_location[0] - self.location[0]) ** 2)
            + ((shop_location[1] - self.location[1]) ** 2)
        ) ** 0.5
        return self.car.fuel_consumption / 100.0 * distance * fuel_price * 2

    def go_shopping(self, fuel_price: float, shops: list[Shop]) -> None:
        print(f"{self.name} has {self.money} dollars")
        cheapest_shop = None
        minimum_total_cost = float("inf")

        for shop in shops:
            trip_cost = self.calculate_trip_cost(shop.location, fuel_price)
            products_cost = shop.calculate_products_cost(self.product_cart)
            total_cost = trip_cost + products_cost

            print(f"{self.name}'s trip to the {shop.name} "
                  f"costs {total_cost:.2f}")  # noqa: E231

            if total_cost < self.money and total_cost < minimum_total_cost:
                cheapest_shop = shop
                minimum_total_cost = total_cost

        if cheapest_shop and self.money >= minimum_total_cost:
            products_cost = cheapest_shop.calculate_products_cost(
                self.product_cart
            )
            self.money -= minimum_total_cost
            print(f"{self.name} rides to {cheapest_shop.name}")
            cheapest_shop.print_receipt(
                self.name,
                self.product_cart,
                products_cost
            )
            print(f"{self.name} rides home")
            print(f"{self.name} now has {self.money:.2f}"  # noqa: E231
                  f" dollars\n")
        else:
            print(f"{self.name} doesn't have enough money "
                  f"to make a purchase in any shop")

from math import sqrt
from app.classes.car import Car
from app.classes.shop import Shop


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
        self.location = location
        self.product_cart = product_cart
        self.money = money
        self.car = Car(**car)

    def calculate_trip_cost(self, shop: Shop, fuel_price: float) -> float:
        distance = sqrt(pow(self.location[0] - shop.location[0], 2)
                        + pow(self.location[1] - shop.location[1], 2))
        fuel_cost = ((self.car.fuel_consumption / 100)
                     * fuel_price * distance * 2)
        cost_of_products = sum(
            amount * shop.products[product]
            for product, amount in self.product_cart.items()
            if product in shop.products
        )
        return round(fuel_cost + cost_of_products, 2)

    def trip_to_the_shop_info(self, shop: Shop, fuel_price: float) -> None:
        print(
            f"{self.name}'s trip to the {shop.name} "
            f"costs {self.calculate_trip_cost(shop, fuel_price)}"
        )

    def ride_for_products(self, shop: Shop, fuel_price: float) -> None:
        print(f"{self.name} rides to {shop.name}\n")
        print(shop.print_receipt(self.name, self.product_cart) + "\n")
        print(
            f"{self.name} rides home\n"
            f"{self.name} now has "
            f"{self.money - self.calculate_trip_cost(shop, fuel_price)} "
            f"dollars\n"
        )

    def money_comparison_and_shopping(
            self,
            min_trip_cost: int | float,
            shop: Shop,
            fuel_price: float
    ) -> None:
        if self.money < min_trip_cost:
            print(
                f"{self.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )
        else:
            self.ride_for_products(shop, fuel_price)

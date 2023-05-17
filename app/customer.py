from datetime import datetime

from app.shop import Shop


class Customer:
    def __init__(
        self,
        name: str,
        product_cart: dict,
        location: list,
        money: int | float,
        car: dict,
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def calculate_distance_cost(
        self, shop: Shop, price_per_liter: int | float
    ) -> float:
        distance = (
            (shop.location[0] - self.location[0]) ** 2
            + (shop.location[1] - self.location[1]) ** 2
        ) ** 0.5
        road_cost = distance * self.car[
            "fuel_consumption"
        ] / 100 * price_per_liter
        return round(road_cost * 2, 2)

    def calculate_product_cost(self, shop: Shop) -> float | int:
        return sum(
            self.product_cart[product] * shop.products[product]
            for product in shop.products
        )

    def calculate_distance_and_product(
            self,
            shop: Shop,
            price_per_liter: int | float
    ) -> int | float:
        return round(
            self.calculate_distance_cost(
                shop,
                price_per_liter
            )
            + self.calculate_product_cost(shop),
            2,
        )

    def calculate_trip_cost(
            self,
            shops: list,
            price_per_liter: float | int
    ) -> None:
        home = self.location
        cheapest_trip = [
            shops[0],
            self.calculate_distance_and_product(shops[0], price_per_liter),
        ]
        print(f"{self.name} has {self.money} dollars")

        for shop in shops:
            trip_price = self.calculate_distance_and_product(
                shop,
                price_per_liter
            )

            print(f"{self.name}'s trip to the {shop.name} costs {trip_price}")

            if cheapest_trip[1] > trip_price:
                cheapest_trip[0], cheapest_trip[1] = shop, trip_price

        if cheapest_trip[1] > self.money:
            print(
                f"{self.name} doesn't have enough money"
                f" to make purchase in any shop"
            )
            return

        print(f"{self.name} rides to {cheapest_trip[0].name}\n")
        self.location = cheapest_trip[0].location

        date = datetime(2021, 1, 4, 12, 33, 41).strftime("%d/%m/%Y %H:%M:%S")
        print(
            f"Date: {date}\n"
            f"Thanks, {self.name}, for you purchase!\n"
            f"You have bought: "
        )

        purchase = 0
        for product in cheapest_trip[0].products:
            price = cheapest_trip[0].products[product] * self.product_cart[product]  # noqa:E126, E501
            print(
                f"{self.product_cart[product]} {product}s "
                f"for {price} dollars"
            )
            purchase += price

        print(
            f"Total cost is {purchase} dollars\n"
            f"See you again!\n\n"
            f"{self.name} rides home\n"
            f"{self.name} now has {self.money - cheapest_trip[1]} dollars\n"
        )
        self.location = home
